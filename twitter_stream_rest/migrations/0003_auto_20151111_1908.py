# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_stream_rest', '0002_auto_20151111_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geotwitter',
            name='id_twitter',
        ),
        migrations.RemoveField(
            model_name='geotwitter',
            name='text_twitter',
        ),
        migrations.RemoveField(
            model_name='geotwitter',
            name='user_avatar',
        ),
        migrations.RemoveField(
            model_name='geotwitter',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='geotwitter',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='geotwitter',
            name='user_screen_name',
        ),
        migrations.AddField(
            model_name='geotwitter',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='geotwitter',
            name='sender_avatar',
            field=models.URLField(max_length=250, null=True, verbose_name='Sender Avatar '),
        ),
        migrations.AddField(
            model_name='geotwitter',
            name='sender_id',
            field=models.CharField(max_length=50, null=True, verbose_name='sender id'),
        ),
        migrations.AddField(
            model_name='geotwitter',
            name='sender_name',
            field=models.CharField(max_length=100, null=True, verbose_name='sender Name'),
        ),
        migrations.AddField(
            model_name='geotwitter',
            name='sender_screen_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Sender scream name'),
        ),
        migrations.AddField(
            model_name='geotwitter',
            name='twitter_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Twitter id'),
        ),
        migrations.AddField(
            model_name='geotwitter',
            name='twitter_text',
            field=models.TextField(max_length=50, null=True, verbose_name='twitter text'),
        ),
        migrations.AddField(
            model_name='monitortwitter',
            name='last_searched_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='monitortwitter',
            name='search_term',
            field=models.CharField(max_length=100, null=True, verbose_name='Search term'),
        ),
        migrations.AlterField(
            model_name='accounttwitter',
            name='user',
            field=models.OneToOneField(related_name='account_twitter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='monitortwitter',
            name='description',
            field=models.CharField(max_length=300, null=True, verbose_name='Description'),
        ),
    ]
