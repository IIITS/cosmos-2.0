# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20170124_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='room',
        ),
        migrations.AddField(
            model_name='time',
            name='room',
            field=models.ManyToManyField(to='polls.Room'),
        ),
    ]
