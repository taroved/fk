# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20150301_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='accreditationpage',
            name='thank_you_text',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accreditationpage',
            name='thank_you_text_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accreditationpage',
            name='thank_you_text_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
