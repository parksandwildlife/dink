# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-06 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0056_auto_20180904_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='mooringsitebooking',
            name='from_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mooringsitebooking',
            name='to_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
