# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foti', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foto',
            options={'ordering': ('foto_position',), 'verbose_name_plural': 'Foti'},
        ),
        migrations.AddField(
            model_name='foto',
            name='foto_position',
            field=models.IntegerField(default=0),
        ),
    ]
