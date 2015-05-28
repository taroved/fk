# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_auto_20150528_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirectpage',
            name='link_en',
            field=models.URLField(verbose_name=b'link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='redirectpage',
            name='link_ru',
            field=models.URLField(verbose_name=b'link', blank=True),
            preserve_default=True,
        ),
    ]
