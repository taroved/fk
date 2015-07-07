# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0001_initial'),
        ('wagtailforms', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailsearch', '0001_initial'),
        ('core', '0064_luckycountrypage'),
    ]

    operations = [
        migrations.CreateModel(
            name='LuckyCountryMainPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('is_browsable', models.BooleanField(default=True, help_text='Whether a browsable link to this page will appear in automatically generated menus')),
                ('title_ru', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name=b'title', blank=True)),
                ('title2', wagtail.wagtailcore.fields.RichTextField(help_text="The page title as you'd like it to be seen by the public (not in menu)", max_length=255, null=True, verbose_name=b'second title', blank=True)),
                ('title2_ru', wagtail.wagtailcore.fields.RichTextField(help_text="The page title as you'd like it to be seen by the public (not in menu)", max_length=255, null=True, verbose_name=b'second title', blank=True)),
                ('title2_en', wagtail.wagtailcore.fields.RichTextField(help_text="The page title as you'd like it to be seen by the public (not in menu)", max_length=255, null=True, verbose_name=b'second title', blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
                ('body_ru', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'body', blank=True)),
                ('body_en', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name=b'body', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.RemoveField(
            model_name='luckycountrypage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='LuckyCountryPage',
        ),
    ]
