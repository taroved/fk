# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_auto_20150323_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpage',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newspage',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photoalbumpage',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='presstoppage',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='videopage',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
