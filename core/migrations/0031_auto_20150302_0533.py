# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20150302_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPackagesPageDateRanges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('title_ru', models.CharField(default=b'', max_length=100, blank=True)),
                ('title_en', models.CharField(default=b'', max_length=100, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='date_ranges', to='core.ForumPackagesPage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='forumpackagespageitem',
            name='description',
            field=core.models.SingleLineTextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpackagespageitem',
            name='description_en',
            field=core.models.SingleLineTextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpackagespageitem',
            name='description_ru',
            field=core.models.SingleLineTextField(default=b'', null=True, blank=True),
            preserve_default=True,
        ),
    ]
