# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opere', '0007_initial_ordering'),
        ('facade', '0005_update_homepage_features_to_scritti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='new_homepage_features',
        ),
        migrations.AddField(
            model_name='profile',
            name='old_homepage_features',
            field=models.ManyToManyField(blank=True, help_text='Max of 6!', related_name='facade_old_homepage_features', to='opere.Opera'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='homepage_features',
            field=models.ManyToManyField(blank=True, help_text='Max of 6!', related_name='facade_homepage_features', to='scritti.Scritto'),
        ),
    ]
