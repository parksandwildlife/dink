# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-31 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0053_auto_20180831_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionsrate',
            name='adult_overnight_cost',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AddField(
            model_name='admissionsrate',
            name='children_overnight_cost',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AddField(
            model_name='admissionsrate',
            name='concession_overnight_cost',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AddField(
            model_name='admissionsrate',
            name='family_overnight_cost',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
        migrations.AddField(
            model_name='admissionsrate',
            name='infant_overnight_cost',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
        ),
    ]
