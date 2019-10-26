# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0062_auto_20180820_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('roll_number', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=10)),
                ('a', models.BooleanField(default=False)),
                ('b', models.BooleanField(default=False)),
            ],
        ),
    ]
