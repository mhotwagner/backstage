# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foti', '0004_initial_ordering'),
        ('opere', '0007_initial_ordering'),
        ('scritti', '0004_initial_ordering'),
        ('facade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='homepage_features',
            field=models.ManyToManyField(help_text='Max of 6!', related_name='facade_homepage_features', to='opere.Opera'),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo_features',
            field=models.ManyToManyField(help_text='Max of 6!', related_name='facade_photo_features', to='foti.Foto'),
        ),
        migrations.AddField(
            model_name='profile',
            name='writing_features',
            field=models.ManyToManyField(help_text='Max of 6!', related_name='facade_writing_features', to='scritti.Scritto'),
        ),
    ]
