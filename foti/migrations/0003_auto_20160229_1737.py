# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foti', '0002_auto_20160229_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foto',
            options={'ordering': ('foto_index',), 'verbose_name_plural': 'Foti'},
        ),
        migrations.RenameField(
            model_name='foto',
            old_name='foto_position',
            new_name='foto_index',
        ),
    ]