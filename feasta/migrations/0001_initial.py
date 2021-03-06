# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-08 18:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.TextField(default='Feasta | Mess @ IIITS')),
            ],
        ),
        migrations.CreateModel(
            name='BulkRedemption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_time', models.DateTimeField(auto_now_add=True)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(b'BF', b'Break Fast'), (b'L', b'Lunch'), (b'D', b'Dinner')], max_length=50)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[(b'SUN', b'Sunday'), (b'MON', b'Monday'), (b'TUE', b'Tuesday'), (b'WED', b'Wednesday'), (b'THU', b'Thursday'), (b'FRI', b'Friday'), (b'SAT', b'Saturday')], max_length=20)),
                ('items', models.TextField(default='NA')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feasta.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vendors', models.TextField(default='NA')),
                ('description', models.TextField(default='NA')),
            ],
        ),
        migrations.CreateModel(
            name='Redemption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_time', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField()),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feasta.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(choices=[(b'2016', b'2016'), (b'2017', b'2017'), (b'2018', b'2018'), (b'2019', b'2019'), (b'2020', b'2020'), (b'2021', b'2021'), (b'2022', b'2022'), (b'2023', b'2023'), (b'2024', b'2024'), (b'2025', b'2025')], default=2016, max_length=4)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions', models.TextField(default='NA')),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default='NA')),
            ],
        ),
        migrations.CreateModel(
            name='NonStudent',
            fields=[
                ('userentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feasta.UserEntity')),
                ('nstype', models.CharField(choices=[(b'F', b'Faculty'), (b'R', b'Research Student'), (b'S', b'Staff')], max_length=20)),
            ],
            bases=('feasta.userentity', models.Model),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('userentity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feasta.UserEntity')),
                ('rollno', models.CharField(max_length=20)),
                ('batch', models.CharField(choices=[(b'UG1', b'UG1'), (b'UG2', b'UG2'), (b'UG3', b'UG3'), (b'UG4', b'UG4')], max_length=20)),
                ('branch', models.CharField(choices=[(b'CSE', b'CSE'), (b'ECE', b'ECE')], max_length=20)),
            ],
            bases=('feasta.userentity', models.Model),
        ),
        migrations.AddField(
            model_name='userentity',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='session',
            unique_together=set([('year', 'name'), ('startdate', 'enddate')]),
        ),
        migrations.AddField(
            model_name='bulkredemption',
            name='endmeal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endmeal', to='feasta.Meal'),
        ),
        migrations.AddField(
            model_name='bulkredemption',
            name='startmeal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='startmeal', to='feasta.Meal'),
        ),
        migrations.AlterUniqueTogether(
            name='redemption',
            unique_together=set([('booked_by', 'date', 'meal')]),
        ),
        migrations.AlterIndexTogether(
            name='redemption',
            index_together=set([('booked_by', 'meal'), ('booked_by', 'date'), ('date', 'meal')]),
        ),
        migrations.AlterUniqueTogether(
            name='bulkredemption',
            unique_together=set([('booked_by', 'startdate', 'enddate')]),
        ),
    ]
