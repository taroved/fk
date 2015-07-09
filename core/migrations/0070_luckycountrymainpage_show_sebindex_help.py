# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_luckycountryitempreview_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='luckycountrymainpage',
            name='show_sebindex_help',
            field=models.BooleanField(default=False, help_text='Whether a sebindex help text will appear in this page'),
            preserve_default=True,
        ),
    ]
