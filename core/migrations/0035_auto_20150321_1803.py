# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20150321_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpanelpage',
            name='section',
            field=modelcluster.fields.ParentalKey(related_name='panels', on_delete=django.db.models.deletion.SET_NULL, to='core.ProgramSectionPage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='programsectionpage',
            name='forum',
            field=modelcluster.fields.ParentalKey(related_name='sections', on_delete=django.db.models.deletion.SET_NULL, to='core.ForumPage', null=True),
            preserve_default=True,
        ),
    ]
