# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150214_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizerpage',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerpage',
            name='link',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
