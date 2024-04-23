# Generated by Django 5.0.1 on 2024-04-22 21:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpotifyApp', '0002_remove_playlist_duration_remove_playlist_track_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_playlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='track',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='track_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
