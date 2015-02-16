# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20150215_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpagespeaker',
            name='speaker_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.SpeakerPage', null=True),
            preserve_default=True,
        ),
    ]
