# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_remove_forumpage_signup_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacts', models.TextField()),
                ('site', models.ForeignKey(editable=False, to='wagtailcore.Site', unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
