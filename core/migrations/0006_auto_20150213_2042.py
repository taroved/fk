# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_advert'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageAdvertPlacement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('advert', models.ForeignKey(related_name='+', to='core.Advert')),
                ('page', modelcluster.fields.ParentalKey(related_name='advert_placements', to='core.HomePage')),
            ],
            options={
                'verbose_name': 'Advert Placement',
                'verbose_name_plural': 'Advert Placements',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PartnerPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('logo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='speakerpage',
            name='full_name',
        ),
    ]
