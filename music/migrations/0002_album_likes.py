# Generated by Django 3.1.5 on 2021-01-22 23:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='likes',
            field=models.ManyToManyField(related_name='album_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
