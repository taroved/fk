# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_auto_20150819_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpanelpage',
            name='end_time',
            field=models.TimeField(null=True, verbose_name=b'End', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpanelpage',
            name='start_time',
            field=models.TimeField(null=True, verbose_name=b'Start', blank=True),
            preserve_default=True,
        ),
    ]
