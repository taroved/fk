# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20150301_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='allspeakersindexpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allspeakersindexpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contentpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contentpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documentpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumindexpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumindexpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumlocationpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumlocationpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumregistrationpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumregistrationpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumspeakerspage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumspeakerspage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetablepage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumtimetablepage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsindexpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsindexpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newspage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newspage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizerpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizerpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orgpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orgpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participationpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participationpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partnerlistpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partnerlistpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photoalbumpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photoalbumpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoplistpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoplistpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoppage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoppage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radapage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='radapage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speakerpage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='speakerpage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopage',
            name='has_en',
            field=models.BooleanField(default=False, help_text='Is EN translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopage',
            name='has_ru',
            field=models.BooleanField(default=False, help_text='Is RU translation enabled for this Page'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='report_text_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'report text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='report_text_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'report text', blank=True),
            preserve_default=True,
        ),
    ]
