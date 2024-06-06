import re
from pathlib import Path
from datetime import datetime

from django.utils.text import slugify
from django.conf import settings
from celery import app

from .models import Album, Photo


DIRECTORY_FORMAT = r'^(\d{4}-\d{2}-\d{2}) (.*)$'  # "YYYY-MM-DD name name"


# @app.task
def discover_files_and_add():
    if not settings.MEDIA_DISCOVERY_ROOT:
        raise Exception("MEDIA_DISCOVERY_ROOT not set")

    root_path = Path(settings.MEDIA_DISCOVERY_ROOT)
    directories = [x for x in root_path.iterdir() if x.is_dir()]

    for directory in directories:
        re_match = re.match(DIRECTORY_FORMAT, directory.name)
        if re_match:
            album_date = datetime.strptime(re_match[1], '%Y-%m-%d').date()
            album_name = re_match[2]

            try:
                album = Album.objects.get(name=album_name, date=album_date)
            except Album.DoesNotExist:
                album = Album.objects.create(
                    name=album_name, date=album_date, slug=slugify(album_name)
                )
            print(album)
            files = [x for x in directory.iterdir() if x.is_file()]
            for file in files:
                try:
                    photo = Photo.objects.get(album=album, file=file)
                except Photo.DoesNotExist:
                    photo = Photo.objects.create(
                        album=album, file=file
                    )
