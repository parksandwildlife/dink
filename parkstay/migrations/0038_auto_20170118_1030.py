# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 02:30
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0037_auto_20170117_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='wkb_geometry',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='promoarea',
            name='wkb_geometry',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
