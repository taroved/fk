# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20150322_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='programpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='programsectionpage',
            name='section_type',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'PD', 'Panel discussions'), (b'PZ', 'Plenary session')]),
            preserve_default=True,
        ),
    ]
