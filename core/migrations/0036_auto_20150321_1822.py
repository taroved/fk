# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0035_auto_20150321_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('forum', modelcluster.fields.ParentalKey(related_name='programs', on_delete=django.db.models.deletion.SET_NULL, to='core.ForumPage', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RenameField(
            model_name='programsectionpage',
            old_name='forum',
            new_name='program',
        ),
    ]
