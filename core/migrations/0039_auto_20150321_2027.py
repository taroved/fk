# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20150321_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='programsectionpage',
            name='forum_day',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programsectionpage',
            name='end_time',
            field=models.TimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programsectionpage',
            name='start_time',
            field=models.TimeField(),
            preserve_default=True,
        ),
    ]
