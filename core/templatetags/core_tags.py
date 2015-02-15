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


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('core/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    request = context['request']
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        menuitem.active = (False if calling_page is None
                           else calling_page.url.startswith(menuitem.url))
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': request,
    }
