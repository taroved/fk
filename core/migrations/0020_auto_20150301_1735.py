# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_forumspeakerspage_is_browsable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumpagespeaker',
            name='forum_page',
        ),
        migrations.AddField(
            model_name='forumpagespeaker',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='speakers', default=51, to='core.ForumSpeakersPage'),
            preserve_default=False,
        ),
    ]
