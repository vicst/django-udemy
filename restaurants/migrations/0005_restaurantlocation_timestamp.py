# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20171016_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
