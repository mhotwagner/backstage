# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scritti', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scritto',
            options={'ordering': ('scritto_order',), 'verbose_name_plural': 'Scritti'},
        ),
        migrations.AddField(
            model_name='scritto',
            name='scritto_order',
            field=models.IntegerField(default=0),
        ),
    ]
