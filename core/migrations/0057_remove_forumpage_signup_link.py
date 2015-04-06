# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_auto_20150406_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpage',
            name='signup_link',
        ),
    ]
