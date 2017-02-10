# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_room_room_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_booking', models.DateField()),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Room')),
            ],
        ),
        migrations.RemoveField(
            model_name='time',
            name='room',
        ),
        migrations.AddField(
            model_name='book',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.time'),
        ),
    ]