# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-28 08:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0126_auto_20190228_1655'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WildlifeLicenceActivityType',
            new_name='LicenceActivity',
        ),
    ]