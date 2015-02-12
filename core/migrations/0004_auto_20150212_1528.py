# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150212_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialpage',
            name='link',
        ),
        migrations.AddField(
            model_name='photoalbumpage',
            name='link',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopage',
            name='code',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videopage',
            name='link',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
    ]
