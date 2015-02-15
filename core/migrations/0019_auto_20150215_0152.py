# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20150215_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpage',
            name='location_latitude',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_longitude',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_map_address',
        ),
        migrations.AddField(
            model_name='forumpage',
            name='location_map_code',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'map_code', blank=True),
            preserve_default=True,
        ),
    ]
