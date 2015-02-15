# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20150215_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpage',
            name='location_city',
            field=models.CharField(max_length=255, null=True, verbose_name=b'city', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='location_country',
            field=models.CharField(max_length=255, null=True, verbose_name=b'country', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='location_latitude',
            field=models.FloatField(null=True, verbose_name=b'latitude', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='location_logo',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'logo', blank=True, to='wagtailimages.Image', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='location_longitude',
            field=models.FloatField(null=True, verbose_name=b'longitude', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='location_map_address',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'map_address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='location_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='location_street',
            field=models.CharField(max_length=255, null=True, verbose_name=b'street', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumpage',
            name='location_zip_code',
            field=models.CharField(max_length=20, null=True, verbose_name=b'zip_code', blank=True),
            preserve_default=True,
        ),
    ]
