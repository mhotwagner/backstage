# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 17:45
from __future__ import unicode_literals

from django.db import migrations

from scritti.models import Scritto


def set_initial_scritto_ordering(apps, schema_editor):
    order = 0
    for scritto in Scritto.objects.all():
        order += 1
        scritto.scritto_index = order
        scritto.save()


class Migration(migrations.Migration):

    dependencies = [
        ('scritti', '0003_auto_20160229_1737'),
    ]

    operations = [
        migrations.RunPython(set_initial_scritto_ordering, reverse_code=migrations.RunPython.noop),
    ]
