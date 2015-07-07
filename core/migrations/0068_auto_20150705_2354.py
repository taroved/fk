# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_auto_20150705_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='luckycountrycategorypage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='luckycountrycategorypage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'body', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='luckycountrycategorypage',
            name='body_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'body', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='luckycountrycategorypage',
            name='sebindex',
            field=models.IntegerField(default=3, choices=[(3, 'Third sebindex'), (2, 'Second sebindex'), (1, 'First sebindex')]),
            preserve_default=True,
        ),
    ]
