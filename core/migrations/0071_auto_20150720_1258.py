# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_luckycountrymainpage_show_sebindex_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpackagespage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpackagespage',
            name='description_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'description', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpackagespage',
            name='description_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'description', blank=True),
            preserve_default=True,
        ),
    ]
