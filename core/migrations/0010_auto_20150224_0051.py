# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150223_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactspageitem',
            name='page',
        ),
        migrations.DeleteModel(
            name='ContactsPageItem',
        ),
        migrations.AddField(
            model_name='contactspage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspage',
            name='body_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
