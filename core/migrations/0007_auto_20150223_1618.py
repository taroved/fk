# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_forumpagetimetableday'),
    ]

    operations = [
        migrations.AddField(
            model_name='accreditationpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='allspeakersindexpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactspage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contentpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumindexpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forumpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='materialspage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orgpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partnerlistpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='presstoplistpage',
            name='is_browsable',
            field=models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus'),
            preserve_default=True,
        ),
    ]
