# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20150301_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumlocationpage',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumlocationpage',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name=b'name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumlocationpage',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name=b'name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumlocationpage',
            name='city',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumlocationpage',
            name='country',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumlocationpage',
            name='street',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
