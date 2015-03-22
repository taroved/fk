# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20150321_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='programsectionpage',
            name='section_type',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'PD', 'Plenary discussions'), (b'PZ', 'Plenary session')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programsectionpage',
            name='end_time',
            field=models.TimeField(verbose_name=b'End'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programsectionpage',
            name='forum_day',
            field=core.fields.IntegerRangeField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programsectionpage',
            name='start_time',
            field=models.TimeField(verbose_name=b'Start'),
            preserve_default=True,
        ),
    ]
