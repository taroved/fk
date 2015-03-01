# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150228_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccreditationPageFormField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('label', models.CharField(help_text='The label of the form field', max_length=255)),
                ('field_type', models.CharField(max_length=16, choices=[(b'singleline', 'Single line text'), (b'multiline', 'Multi-line text'), (b'email', 'Email'), (b'number', 'Number'), (b'url', 'URL'), (b'checkbox', 'Checkbox'), (b'checkboxes', 'Checkboxes'), (b'dropdown', 'Drop down'), (b'radio', 'Radio buttons'), (b'date', 'Date'), (b'datetime', 'Date/time')])),
                ('required', models.BooleanField(default=True)),
                ('choices', models.CharField(help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', max_length=512, blank=True)),
                ('default_value', models.CharField(help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, blank=True)),
                ('help_text', models.CharField(max_length=255, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='form_fields', to='core.AccreditationPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='accreditationpage',
            name='from_address',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accreditationpage',
            name='subject',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accreditationpage',
            name='to_address',
            field=models.CharField(help_text='Optional - form submissions will be emailed to this address', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
