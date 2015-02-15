# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_homepagematerialvideo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagevideoitem',
            name='page',
        ),
        migrations.RemoveField(
            model_name='homepagevideoitem',
            name='preview',
        ),
        migrations.DeleteModel(
            name='HomePageVideoItem',
        ),
    ]
