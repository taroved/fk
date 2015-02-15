# coding=utf-8
from datetime import date
from django import template
from core.models import SliderItem, Partner, OrganizerPage

register = template.Library()


@register.inclusion_tag('core/tags/slider.html', takes_context=True)
def slider(context):
    return {
        'items': SliderItem.objects.all(),
        'request': context['request'],
    }


@register.inclusion_tag('core/tags/partners.html', takes_context=True)
def partners(context):
    return {
        'partners': Partner.objects.all(),
        'request': context['request'],
    }


@register.inclusion_tag('core/tags/organizers.html', takes_context=True)
def organizers(context):
    return {
        'organizers': OrganizerPage.objects.live().all(),
        'request': context['request'],
    }


@register.simple_tag
def copyright_years(start_year=2015):
    year = date.today().year
    if not start_year == year:
        year_interval = "%s — %s" % (start_year, year)
    else:
        year_interval = str(year)
    return year_interval