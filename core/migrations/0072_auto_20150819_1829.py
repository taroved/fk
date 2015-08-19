# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('core', '0071_auto_20150720_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgCommitteePersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('is_browsable', models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus')),
                ('title_ru', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('about', wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, blank=True)),
                ('about_ru', wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, verbose_name=b'about', blank=True)),
                ('about_en', wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, verbose_name=b'about', blank=True)),
                ('photo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.AlterField(
            model_name='photoalbumpage',
            name='link',
            field=models.URLField(default=b'', help_text=b'example: https://www.flickr.com/photos/129599628@N03/sets/72157650435543677/', validators=[core.models.validate_flickr_album]),
            preserve_default=True,
        ),
    ]
