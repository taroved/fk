# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150301_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accreditationpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'body', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='accreditationpage',
            name='body_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'body', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='accreditationpage',
            name='thank_you_text_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'thank you text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='accreditationpage',
            name='thank_you_text_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'thank you text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partner',
            name='description_en',
            field=models.TextField(null=True, verbose_name=b'description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='partner',
            name='description_ru',
            field=models.TextField(null=True, verbose_name=b'description', blank=True),
            preserve_default=True,
        ),
    ]
