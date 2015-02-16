# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_forumpagetimetableday_timetabledayitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetabledayitem',
            name='day',
            field=modelcluster.fields.ParentalKey(related_name='timetable', default=None, to='core.ForumPageTimetableDay'),
            preserve_default=False,
        ),
    ]
