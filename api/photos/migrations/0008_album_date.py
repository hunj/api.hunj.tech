# Generated by Django 4.2.4 on 2023-11-27 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_alter_event_albums_alter_event_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
