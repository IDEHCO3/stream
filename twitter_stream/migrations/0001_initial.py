# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTwitter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('consumer_key', models.CharField(blank=True, max_length=100, null=True)),
                ('consumer_secret', models.CharField(blank=True, max_length=100, null=True)),
                ('consumer_token', models.CharField(blank=True, max_length=100, null=True)),
                ('consumer_toke_secret', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GeoTwitter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('id_twitter', models.CharField(verbose_name='Id twitter', max_length=50)),
                ('text_twitter', models.TextField(verbose_name='Text twitter', max_length=50)),
                ('user_id', models.CharField(verbose_name='User id', max_length=50)),
                ('user_screen_name', models.CharField(verbose_name='User name', max_length=50)),
                ('user_name', models.CharField(verbose_name='Name', max_length=100)),
                ('user_avatar', models.URLField(verbose_name='User Avatar ', max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MonitorTwitter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=100)),
                ('description', models.CharField(verbose_name='Description', max_length=300)),
                ('initial_date', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('final_date', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('interval', models.CharField(default='01:00:00', max_length=8, help_text='hh:mm:ss')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(verbose_name='User', related_name='col_of_monitor_twitter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='geotwitter',
            name='monitor_twitter',
            field=models.ForeignKey(to='twitter_stream.MonitorTwitter', related_name='geotwitters'),
        ),
    ]
