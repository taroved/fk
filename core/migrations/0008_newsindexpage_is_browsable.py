# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150223_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsindexpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
    ]
