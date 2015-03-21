# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0032_auto_20150304_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('is_browsable', models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus')),
                ('has_ru', models.BooleanField(default=False, help_text='Is RU translation enabled for this Page')),
                ('has_en', models.BooleanField(default=False, help_text='Is EN translation enabled for this Page')),
                ('title_ru', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
                ('body_ru', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'body', blank=True)),
                ('body_en', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'body', blank=True)),
                ('location', models.TextField(null=True, blank=True)),
                ('location_ru', models.TextField(null=True, verbose_name=b'description', blank=True)),
                ('location_en', models.TextField(null=True, verbose_name=b'description', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='ProgramSectionPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('is_browsable', models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus')),
                ('has_ru', models.BooleanField(default=False, help_text='Is RU translation enabled for this Page')),
                ('has_en', models.BooleanField(default=False, help_text='Is EN translation enabled for this Page')),
                ('title_ru', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
