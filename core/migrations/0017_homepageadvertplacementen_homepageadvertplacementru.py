# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20150301_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageAdvertPlacementEN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('advert', models.ForeignKey(related_name='+', to='core.Advert')),
                ('page', modelcluster.fields.ParentalKey(related_name='advert_placements_en', to='core.HomePage')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Advert Placement',
                'verbose_name_plural': 'Advert Placements',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomePageAdvertPlacementRU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('advert', models.ForeignKey(related_name='+', to='core.Advert')),
                ('page', modelcluster.fields.ParentalKey(related_name='advert_placements_ru', to='core.HomePage')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Advert Placement',
                'verbose_name_plural': 'Advert Placements',
            },
            bases=(models.Model,),
        ),
    ]
