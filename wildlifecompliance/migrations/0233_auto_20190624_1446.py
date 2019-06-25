# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-06-24 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0232_auto_20190621_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callemail',
            name='referrer',
        ),
        migrations.AddField(
            model_name='callemail',
            name='referrer',
            field=models.ManyToManyField(blank=True, related_name='report_referrer', to='wildlifecompliance.Referrer'),
        ),
    ]