# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-15 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledgergw', '0002_auto_20200414_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='active',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0),
        ),
    ]