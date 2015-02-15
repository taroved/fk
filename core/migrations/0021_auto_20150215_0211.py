# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20150215_0158'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ForumPageSpeakers',
        ),
        migrations.AddField(
            model_name='forumpagespeaker',
            name='speaker_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', null=True),
            preserve_default=True,
        ),
    ]
