# Generated by Django 4.2.4 on 2023-11-13 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_person_location_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='albums',
            field=models.ManyToManyField(related_name='events', to='photos.album'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='location',
            name='albums',
            field=models.ManyToManyField(related_name='locations', to='photos.album'),
        ),
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='person',
            name='photos',
            field=models.ManyToManyField(related_name='tagged', to='photos.photo'),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photos.album'),
        ),
    ]
