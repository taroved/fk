# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('core', '0049_auto_20150323_0422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radapagemember',
            options={},
        ),
        migrations.RemoveField(
            model_name='radapagemember',
            name='id',
        ),
        migrations.RemoveField(
            model_name='radapagemember',
            name='title',
        ),
        migrations.AddField(
            model_name='radapagemember',
            name='page_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to='wagtailcore.Page'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='radapagemember',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='members', on_delete=django.db.models.deletion.SET_NULL, to='core.RadaPage', null=True),
            preserve_default=True,
        ),
    ]
