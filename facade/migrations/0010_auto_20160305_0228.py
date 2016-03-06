# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 02:28
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facade', '0009_auto_20160305_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(blank=True, max_length=4096),
        ),
        migrations.AlterField(
            model_name='profile',
            name='intro',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1024),
        ),
    ]