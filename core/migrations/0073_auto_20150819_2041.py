# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_auto_20150819_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgcommitteepersonpage',
            name='position',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orgcommitteepersonpage',
            name='position_en',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'position', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orgcommitteepersonpage',
            name='position_ru',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'position', blank=True),
            preserve_default=True,
        ),
    ]
