# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2018-02-16 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0031_heading_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretarie',
            name='fb_link',
            field=models.URLField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='secretarie',
            name='git_link',
            field=models.URLField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='secretarie',
            name='linkedin_link',
            field=models.URLField(blank=True, max_length=50),
        ),
    ]
