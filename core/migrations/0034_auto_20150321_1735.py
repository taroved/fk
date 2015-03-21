# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_panel_programsectionpage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Panel',
            new_name='ForumPanelPage',
        ),
    ]
