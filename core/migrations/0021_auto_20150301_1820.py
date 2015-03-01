# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0020_auto_20150301_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumLocationPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('is_browsable', models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus')),
                ('title_ru', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('city', models.CharField(max_length=255, null=True, verbose_name=b'city', blank=True)),
                ('city_ru', models.CharField(max_length=255, null=True, verbose_name=b'city', blank=True)),
                ('city_en', models.CharField(max_length=255, null=True, verbose_name=b'city', blank=True)),
                ('street', models.CharField(max_length=255, null=True, verbose_name=b'street', blank=True)),
                ('street_ru', models.CharField(max_length=255, null=True, verbose_name=b'street', blank=True)),
                ('street_en', models.CharField(max_length=255, null=True, verbose_name=b'street', blank=True)),
                ('country', models.CharField(max_length=255, null=True, verbose_name=b'country', blank=True)),
                ('country_ru', models.CharField(max_length=255, null=True, verbose_name=b'country', blank=True)),
                ('country_en', models.CharField(max_length=255, null=True, verbose_name=b'country', blank=True)),
                ('zip_code', models.CharField(max_length=20, null=True, verbose_name=b'zip_code', blank=True)),
                ('map_code', models.CharField(default=b'', max_length=255, verbose_name=b'map_code', blank=True)),
                ('logo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_city',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_city_en',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_city_ru',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_country',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_country_en',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_country_ru',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_logo',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_map_code',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_name',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_name_en',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_name_ru',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_street',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_street_en',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_street_ru',
        ),
        migrations.RemoveField(
            model_name='forumpage',
            name='location_zip_code',
        ),
        migrations.AlterField(
            model_name='forumpagespeaker',
            name='speaker_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'speaker', blank=True, to='core.SpeakerPage', null=True),
            preserve_default=True,
        ),
    ]
