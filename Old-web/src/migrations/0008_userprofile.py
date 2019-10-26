# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 14:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('src', '0007_remove_about_us_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('desciption', models.CharField(default='', max_length=500)),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='')),
                ('user_type', models.CharField(choices=[('btec', 'B.TECH'), ('mtec', 'M.TECH'), ('tea', 'teacher'), ('rst', 'Reaserch Student')], max_length=4)),
                ('user_year', models.CharField(choices=[('1st', '1st Year Student'), ('2nd', '2nd Year Student'), ('3rd', 'Third Year Student'), ('4th', '4th Year Student'), ('phd', 'PHD'), ('fac', 'Faculty')], default='1st', max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
