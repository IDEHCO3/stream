# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('spatial', models.CharField(max_length=255, null=True, choices=[(b'Geometry', b'geometry')])),
            ],
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute', models.CharField(max_length=255)),
                ('means', models.CharField(default=b'http://schema.org/Thing', max_length=1000)),
                ('type', models.CharField(max_length=1000, null=True, blank=True)),
                ('classname', models.ForeignKey(related_name='contexts', to='context_api.Class')),
            ],
        ),
    ]
