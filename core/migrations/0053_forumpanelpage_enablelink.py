# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20150323_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpanelpage',
            name='enableLink',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
