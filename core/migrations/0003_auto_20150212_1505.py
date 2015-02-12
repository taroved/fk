# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtaildocs', '0002_initial_data'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0002_auto_20150209_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.TextField(default=b'')),
                ('link', models.URLField(default=b'')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DocumentPage',
            fields=[
                ('materialpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.MaterialPage')),
                ('doc', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtaildocs.Document', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.materialpage',),
        ),
        migrations.CreateModel(
            name='PhotoAlbumPage',
            fields=[
                ('materialpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.MaterialPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.materialpage',),
        ),
        migrations.CreateModel(
            name='VideoPage',
            fields=[
                ('materialpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.MaterialPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.materialpage',),
        ),
        migrations.AddField(
            model_name='materialpage',
            name='preview',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
            preserve_default=True,
        ),
    ]
