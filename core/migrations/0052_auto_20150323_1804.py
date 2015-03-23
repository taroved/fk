# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0051_auto_20150323_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadaMemberPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('is_browsable', models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus')),
                ('title_ru', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('position', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('position_ru', models.CharField(default=b'', max_length=255, null=True, verbose_name=b'position', blank=True)),
                ('position_en', models.CharField(default=b'', max_length=255, null=True, verbose_name=b'position', blank=True)),
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
        migrations.RemoveField(
            model_name='radapagemember',
            name='page',
        ),
        migrations.RemoveField(
            model_name='radapagemember',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='radapagemember',
            name='photo',
        ),
        migrations.DeleteModel(
            name='RadaPageMember',
        ),
    ]
