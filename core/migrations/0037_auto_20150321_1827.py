# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20150321_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpanelpage',
            name='section',
        ),
        migrations.RemoveField(
            model_name='programpage',
            name='forum',
        ),
        migrations.RemoveField(
            model_name='programsectionpage',
            name='program',
        ),
    ]
