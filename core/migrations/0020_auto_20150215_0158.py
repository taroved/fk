# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150215_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumlocationpage',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='forumlocationpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='ForumLocationPage',
        ),
        migrations.AlterField(
            model_name='forumtimetableitem',
            name='time_from',
            field=models.DateTimeField(null=True, verbose_name=b'Start time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='forumtimetableitem',
            name='time_to',
            field=models.DateTimeField(null=True, verbose_name=b'End time', blank=True),
            preserve_default=True,
        ),
    ]
