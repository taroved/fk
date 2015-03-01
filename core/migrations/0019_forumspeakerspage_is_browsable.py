# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_forumspeakerspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumspeakerspage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
    ]
