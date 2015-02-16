# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_forumpagedocument_forumpagephotoalbum_forumpagevideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPageDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('doc', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.DocumentPage', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='documents', to='core.NewsPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsPagePhotoAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('album', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.PhotoAlbumPage', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='albums', to='core.NewsPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsPageVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='videos', to='core.NewsPage')),
                ('video', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.VideoPage', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
