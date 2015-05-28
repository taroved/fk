# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_auto_20150412_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirectpage',
            name='link_en',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='redirectpage',
            name='link_ru',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpanelpage',
            name='location_en',
            field=models.CharField(max_length=255, null=True, verbose_name=b'location', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpanelpage',
            name='location_ru',
            field=models.CharField(max_length=255, null=True, verbose_name=b'location', blank=True),
            preserve_default=True,
        ),
    ]
