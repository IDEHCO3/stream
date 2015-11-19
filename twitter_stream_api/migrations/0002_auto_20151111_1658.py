# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_stream_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounttwitter',
            old_name='consumer_toke_secret',
            new_name='consumer_token_secret',
        ),
        migrations.AddField(
            model_name='monitortwitter',
            name='since_id',
            field=models.BigIntegerField(default=0, verbose_name='Since id', editable=False),
        ),
    ]
