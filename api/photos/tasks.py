from django.conf import settings
from celery import app

from .models import Album, Photo


@app.task
def discover_files_and_add():
    if not settings.MEDIA_DISCOVERY_ROOT:
        raise Exception("MEDIA_DISCOVERY_ROOT not set")

    ...