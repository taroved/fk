# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20150301_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialspage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='materialspage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
    ]
