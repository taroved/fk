# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20150323_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='radapagemember',
            name='sort_order',
        ),
        migrations.AddField(
            model_name='radapagemember',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
    ]
