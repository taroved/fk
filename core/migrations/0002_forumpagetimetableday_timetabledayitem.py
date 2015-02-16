# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPageTimetableDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='timetable_days', to='core.ForumPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimetableDayItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255, blank=True)),
                ('time_from', models.TimeField(null=True, verbose_name=b'Start time', blank=True)),
                ('time_to', models.TimeField(null=True, verbose_name=b'End time', blank=True)),
                ('location', models.CharField(default=b'', max_length=255, blank=True)),
                ('description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('day', models.ForeignKey(related_name='timetable', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.TimetableDayItem', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
