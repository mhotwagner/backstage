# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facade', '0007_remove_profile_old_homepage_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio_photo',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
