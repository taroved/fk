# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20150322_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='programpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='programpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='programpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='programpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True),
            preserve_default=True,
        ),
    ]
