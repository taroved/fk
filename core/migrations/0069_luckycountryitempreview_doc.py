# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0002_initial_data'),
        ('core', '0068_auto_20150705_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='luckycountryitempreview',
            name='doc',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtaildocs.Document', null=True),
            preserve_default=True,
        ),
    ]
