# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('context_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupportedOperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=1000, null=True, blank=True)),
                ('type', models.CharField(max_length=100, blank=True)),
                ('title', models.CharField(max_length=100)),
                ('method', models.CharField(max_length=100)),
                ('possible_status', models.CharField(max_length=100, null=True, blank=True)),
                ('expects', models.ForeignKey(related_name='operations_expects', to='context_api.Class', null=True)),
                ('hydra_class', models.ForeignKey(related_name='supported_operations', to='context_api.Class')),
                ('returns', models.ForeignKey(related_name='operations_returns', to='context_api.Class', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupportedProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property', models.CharField(max_length=100)),
                ('required', models.BooleanField()),
                ('readable', models.BooleanField()),
                ('writeable', models.BooleanField()),
                ('hydra_class', models.ForeignKey(related_name='supported_properties', to='context_api.Class')),
            ],
        ),
    ]
