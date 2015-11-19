# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_stream_api', '0004_remove_geotwitter_geom'),
    ]

    operations = [
        migrations.AddField(
            model_name='geotwitter',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326, null=True),
        ),
    ]
