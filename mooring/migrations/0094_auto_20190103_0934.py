# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-03 01:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0093_auto_20190103_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='globalsettings',
            options={'verbose_name_plural': 'Global Settings'},
        ),
        migrations.AlterModelOptions(
            name='registeredvessels',
            options={'verbose_name_plural': 'Global Settings'},
        ),
    ]
