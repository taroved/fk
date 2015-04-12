# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_socialmediasettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentpage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='photoalbumpage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='videopage',
            name='description',
        ),
    ]
