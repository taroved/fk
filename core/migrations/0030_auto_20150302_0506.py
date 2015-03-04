# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0029_materialsalbumspage_materialsdocumentspage_materialsvideopage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPackagesPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('is_browsable', models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus')),
                ('has_ru', models.BooleanField(default=False, help_text='Is RU translation enabled for this Page')),
                ('has_en', models.BooleanField(default=False, help_text='Is EN translation enabled for this Page')),
                ('title_ru', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='ForumPackagesPageItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('title_ru', models.CharField(default=b'', max_length=100, blank=True)),
                ('title_en', models.CharField(default=b'', max_length=100, blank=True)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('description_ru', models.TextField(default=b'', null=True, blank=True)),
                ('description_en', models.TextField(default=b'', null=True, blank=True)),
                ('prices', models.CommaSeparatedIntegerField(max_length=100, null=True, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='packages', to='core.ForumPackagesPage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='forumindexpage',
            options={'verbose_name': 'Forum Archive Page'},
        ),
    ]
