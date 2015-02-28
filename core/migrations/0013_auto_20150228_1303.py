# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150224_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentpage',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photoalbumpage',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videopage',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'date'),
            preserve_default=False,
        ),
    ]
