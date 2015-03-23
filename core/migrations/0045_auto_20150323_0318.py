# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20150323_0303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspage',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='body_ru',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='is_browsable',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='short_en',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='short_ru',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='newspage',
            name='title_ru',
        ),
        migrations.AddField(
            model_name='newspage',
            name='language',
            field=models.CharField(default=b'uk', max_length=2, choices=[(b'uk', 'Ukrainian'), (b'ru', 'Russian'), (b'en', 'English')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newspage',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
