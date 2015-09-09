# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_auto_20150831_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('html', models.TextField(null=True, blank=True)),
                ('html_ru', models.TextField(null=True, verbose_name=b'html', blank=True)),
                ('html_en', models.TextField(null=True, verbose_name=b'html', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
