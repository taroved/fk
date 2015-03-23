# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20150323_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetabledayitem',
            name='day',
        ),
        migrations.DeleteModel(
            name='TimetableDayItem',
        ),
    ]
