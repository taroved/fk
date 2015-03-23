# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_auto_20150323_0355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accreditationpage',
            name='has_en',
        ),
        migrations.RemoveField(
            model_name='accreditationpage',
            name='has_ru',
        ),
    ]
