# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_forumpagedocument_forumpagephotoalbum'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPageTimetableDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(default=b'', max_length=255, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='timetable_days', to='core.ForumPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
