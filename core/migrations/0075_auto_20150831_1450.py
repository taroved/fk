# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_auto_20150820_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slideritem',
            name='button_link',
        ),
        migrations.RemoveField(
            model_name='slideritem',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='slideritem',
            name='button_text_en',
        ),
        migrations.RemoveField(
            model_name='slideritem',
            name='button_text_ru',
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='text',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='text_en',
            field=models.TextField(null=True, verbose_name=b'text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='text_ru',
            field=models.TextField(null=True, verbose_name=b'text', blank=True),
            preserve_default=True,
        ),
    ]
