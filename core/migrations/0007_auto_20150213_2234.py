# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailredirects', '0001_initial'),
        ('wagtailforms', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailsearch', '0001_initial'),
        ('core', '0006_auto_20150213_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumLocationPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('street', models.CharField(max_length=255, null=True, blank=True)),
                ('country', models.CharField(max_length=255, null=True, blank=True)),
                ('zip_code', models.IntegerField(max_length=20, null=True, blank=True)),
                ('location', models.CharField(default=b'', max_length=255, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('logo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ForumPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_long', models.CharField(default=b'', max_length=100, blank=True)),
                ('date_from', models.DateField(verbose_name=b'Start date')),
                ('date_to', models.DateField(help_text=b'Not required if event is on a single day', null=True, verbose_name=b'End date', blank=True)),
                ('description', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('signup_link', models.URLField(blank=True)),
                ('has_report', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RenameModel(
            old_name='EventIndexPage',
            new_name='ForumIndexPage',
        ),
        migrations.RenameModel(
            old_name='EventTimetableItem',
            new_name='ForumTimetableItem',
        ),
        migrations.RenameModel(
            old_name='EventTimetablePage',
            new_name='ForumTimetablePage',
        ),
        migrations.RemoveField(
            model_name='eventlocationpage',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='eventlocationpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='EventLocationPage',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='eventpagespeaker',
            name='event_page',
        ),
        migrations.DeleteModel(
            name='EventPage',
        ),
        migrations.DeleteModel(
            name='EventPageSpeaker',
        ),
    ]
