# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_forumpanelpage_enablelink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumpanelpage',
            old_name='enableLink',
            new_name='enable_link',
        ),
    ]
