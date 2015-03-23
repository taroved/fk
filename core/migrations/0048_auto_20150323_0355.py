# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20150323_0352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presstoppage',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='presstoppage',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='presstoppage',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='presstoppage',
            name='description_ru',
        ),
    ]
