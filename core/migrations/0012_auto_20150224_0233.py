# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailredirects', '0001_initial'),
        ('wagtailforms', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailsearch', '0001_initial'),
        ('core', '0011_radamember'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadaPageMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title_ru', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('position', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('position_ru', models.CharField(default=b'', max_length=255, null=True, verbose_name=b'position', blank=True)),
                ('position_en', models.CharField(default=b'', max_length=255, null=True, verbose_name=b'position', blank=True)),
                ('about', wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, blank=True)),
                ('about_ru', wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, verbose_name=b'about', blank=True)),
                ('about_en', wagtail.wagtailcore.fields.RichTextField(default=b'', null=True, verbose_name=b'about', blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='members', to='core.RadaPage')),
                ('photo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='radamember',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='radamember',
            name='photo',
        ),
        migrations.DeleteModel(
            name='RadaMember',
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='button_text_en',
            field=models.CharField(max_length=50, null=True, verbose_name=b'button text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='button_text_ru',
            field=models.CharField(max_length=50, null=True, verbose_name=b'button text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='text_en',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='text_ru',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'text', blank=True),
            preserve_default=True,
        ),
    ]
