# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 17:54
from __future__ import unicode_literals

from django.db import migrations

from foti.models import Foto


def set_initial_foto_ordering(apps, schema_editor):
    order = 0
    for foto in Foto.objects.all():
        order += 1
        foto.foto_index = order
        foto.save()


class Migration(migrations.Migration):

    dependencies = [
        ('foti', '0003_auto_20160229_1737'),
    ]

    operations = [
        migrations.RunPython(set_initial_foto_ordering, reverse_code=migrations.RunPython.noop),
    ]
