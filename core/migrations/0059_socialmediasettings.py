# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_contactssettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook', models.URLField(help_text=b'Your Facebook page URL')),
                ('flickr', models.URLField(help_text=b'Your flickr album')),
                ('youtube', models.URLField(help_text=b'Your YouTube channel or user account URL')),
                ('site', models.ForeignKey(editable=False, to='wagtailcore.Site', unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
