# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20150322_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpanelpage',
            name='location',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpanelpage',
            name='location_en',
            field=models.CharField(max_length=255, null=True, verbose_name=b'description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpanelpage',
            name='location_ru',
            field=models.CharField(max_length=255, null=True, verbose_name=b'description', blank=True),
            preserve_default=True,
        ),
    ]
