# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accreditationpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accreditationpage',
            name='body_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accreditationpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accreditationpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allspeakersindexpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allspeakersindexpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspageitem',
            name='info_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspageitem',
            name='info_ru',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspageitem',
            name='title_en',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspageitem',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contentpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contentpage',
            name='body_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contentpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contentpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentpage',
            name='description_en',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentpage',
            name='description_ru',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumindexpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumindexpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='description_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='description_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='location_city_en',
            field=models.CharField(max_length=255, null=True, verbose_name=b'city', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='location_city_ru',
            field=models.CharField(max_length=255, null=True, verbose_name=b'city', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='location_country_en',
            field=models.CharField(max_length=255, null=True, verbose_name=b'country', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='location_country_ru',
            field=models.CharField(max_length=255, null=True, verbose_name=b'country', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='location_name_en',
            field=models.CharField(max_length=255, null=True, verbose_name=b'name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='location_name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name=b'name', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='location_street_en',
            field=models.CharField(max_length=255, null=True, verbose_name=b'street', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='location_street_ru',
            field=models.CharField(max_length=255, null=True, verbose_name=b'street', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='report_text_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='report_text_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='title_long_en',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='title_long_ru',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetableitem',
            name='description_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetableitem',
            name='description_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetableitem',
            name='location_en',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetableitem',
            name='location_ru',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetableitem',
            name='title_en',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetableitem',
            name='title_ru',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetablepage',
            name='comment_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetablepage',
            name='comment_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetablepage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetablepage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newspage',
            name='body_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newspage',
            name='body_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newspage',
            name='short_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newspage',
            name='short_ru',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newspage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newspage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizerpage',
            name='description_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizerpage',
            name='description_ru',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizerpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizerpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orgpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orgpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participationpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participationpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partner',
            name='description_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partner',
            name='description_ru',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partner',
            name='title_en',
            field=models.CharField(help_text="The title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partner',
            name='title_ru',
            field=models.CharField(help_text="The title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partnerlistpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partnerlistpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photoalbumpage',
            name='description_en',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photoalbumpage',
            name='description_ru',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photoalbumpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photoalbumpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoplistpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoplistpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoppage',
            name='content_en',
            field=wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoppage',
            name='content_ru',
            field=wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoppage',
            name='description_en',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoppage',
            name='description_ru',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoppage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoppage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radapage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radapage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideritem',
            name='button_text_en',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideritem',
            name='button_text_ru',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideritem',
            name='text_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slideritem',
            name='text_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speakerpage',
            name='about_en',
            field=wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speakerpage',
            name='about_ru',
            field=wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speakerpage',
            name='position_en',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speakerpage',
            name='position_ru',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speakerpage',
            name='title_en',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speakerpage',
            name='title_ru',
            field=models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopage',
            name='description_en',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopage',
            name='description_ru',
            field=models.TextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
