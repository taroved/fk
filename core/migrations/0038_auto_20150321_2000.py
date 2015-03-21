# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20150321_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programsectionpage',
            old_name='time',
            new_name='start_time',
        ),
        migrations.RemoveField(
            model_name='forumpanelpage',
            name='sort_order',
        ),
        migrations.RemoveField(
            model_name='programsectionpage',
            name='sort_order',
        ),
        migrations.AddField(
            model_name='programsectionpage',
            name='end_time',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
