# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-03-29 07:39
from __future__ import unicode_literals

import commercialoperator.components.compliances.models
import commercialoperator.components.proposals.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0060_auto_20190329_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProposalOtherDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accreditation_type', models.CharField(choices=[('no', 'No'), ('atap', 'ATAP'), ('eco_certification', 'Eco Certification'), ('narta', 'NARTA')], default='no', max_length=40, verbose_name='Accreditation')),
                ('accreditation_expiry', models.DateTimeField(blank=True, null=True)),
                ('preferred_license_period', models.CharField(choices=[('2_months', '2 months'), ('1_year', '1 Year'), ('3_year', '3 Years'), ('5_year', '5 Years'), ('7_year', '7 Years'), ('10_year', '10 Years')], default='2_months', max_length=40, verbose_name='Preferred license period')),
                ('nominated_start_date', models.DateTimeField(blank=True, null=True)),
                ('insurance_expiry', models.DateTimeField(blank=True, null=True)),
                ('other_comments', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
        migrations.AlterField(
            model_name='proposalrequireddocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.proposals.models.update_proposal_required_doc_filename),
        ),
    ]