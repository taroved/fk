# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20150302_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumlocationpage',
            name='link',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpackagespageitem',
            name='description_en',
            field=core.models.SingleLineTextField(default=b'', null=True, verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpackagespageitem',
            name='description_ru',
            field=core.models.SingleLineTextField(default=b'', null=True, verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpackagespageitem',
            name='title_en',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'title', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpackagespageitem',
            name='title_ru',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'title', blank=True),
            preserve_default=True,
        ),
    ]
