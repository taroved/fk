# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailsearch', '0001_initial'),
        ('wagtailredirects', '0001_initial'),
        ('wagtailforms', '0001_initial'),
        ('core', '0014_forumpagespeakers_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizerPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('link', models.URLField()),
                ('description', models.TextField()),
                ('logo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='OrganizatorPage',
        ),
        migrations.DeleteModel(
            name='PartnerPage',
        ),
    ]
