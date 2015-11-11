# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_stream', '0003_auto_20151111_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geotwitter',
            name='geom',
        ),
    ]
