# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 03:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opere', '0001_initial'),
        ('foti', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='created',
        ),
        migrations.RemoveField(
            model_name='foto',
            name='id',
        ),
        migrations.RemoveField(
            model_name='foto',
            name='image',
        ),
        migrations.RemoveField(
            model_name='foto',
            name='name',
        ),
        migrations.RemoveField(
            model_name='foto',
            name='updated',
        ),
        migrations.AddField(
            model_name='foto',
            name='opera_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='opere.Opera'),
            preserve_default=False,
        ),
    ]
