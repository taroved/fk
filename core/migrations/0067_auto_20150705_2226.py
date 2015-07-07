# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_luckycountrycategorypage_luckycountryitempreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='luckycountrycategorypage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='luckycountrycategorypage',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='luckycountrycategorypage',
            name='body_ru',
        ),
    ]
