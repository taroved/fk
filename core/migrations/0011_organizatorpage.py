# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_partnerlistpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizatorPage',
            fields=[
                ('partnerpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.PartnerPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.partnerpage',),
        ),
    ]
