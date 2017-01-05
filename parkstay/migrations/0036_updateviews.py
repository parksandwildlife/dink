# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-02 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0035_auto_20161228_1735'),
    ]

    operations = [
        migrations.RunSQL(
            """CREATE OR REPLACE VIEW parkstay_campsiteclass_pricehistory_v AS
                    SELECT DISTINCT classes.campsite_class_id AS id,
                        classes.date_start,
                        classes.date_end,
                        r.id AS rate_id,
                        r.adult,
                        r.concession,
                        r.child,
                        classes.details,
                        classes.reason_id,
                        r.infant
                    FROM parkstay_rate r
                    INNER JOIN (
                        SELECT distinct cc.id AS campsite_class_id,
                            cr.rate_id AS campsite_rate_id,
                            cr.date_start AS date_start,
                            cr.date_end AS date_end,
                            cr.details AS details,
                            cr.reason_id AS reason_id
                        FROM parkstay_campsite cs,
                            parkstay_campsiteclass cc,
                            parkstay_campsiterate cr
                        WHERE cs.campsite_class_id = cc.id AND
                            cr.campsite_id = cs.id AND
                            cr.update_level = 1
                    ) classes ON r.id = classes.campsite_rate_id"""
        ),
        migrations.RunSQL(
            """CREATE OR REPLACE VIEW parkstay_campground_pricehistory_v AS
                    SELECT DISTINCT camps.campground_id AS id,
                        cr.date_start,
                        cr.date_end,
                        r.id AS rate_id,
                        r.adult,
                        r.concession,
                        r.child,
                        cr.details,
                        cr.reason_id,
                        r.infant
                    FROM parkstay_campsiterate cr
                    INNER JOIN parkstay_rate r ON r.id = cr.rate_id
                    INNER JOIN (
                        SELECT cg.id AS campground_id,
                            cs.name AS name,
                            cs.id AS campsite_id
                        FROM parkstay_campsite cs,
                            parkstay_campground cg
                        WHERE cs.campground_id = cg.id AND
                            cg.id = cs.campground_id AND
                            cg.price_level = 0
                    ) camps ON cr.campsite_id = camps.campsite_id"""
        )
    ]
