# coding=utf-8
from datetime import date
from django import template
from django.template import Node, Variable
from django.template.base import render_value_in_context
from django.utils import translation
import six
from wagtail.wagtailcore.models import Page
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


@register.simple_tag
def trans_field(instance, field):
    lang_code = translation.get_language()
    trans_field_name = '%s_%s' % (field, lang_code)
    specific = instance.specific if isinstance(instance, Page) else instance
    if hasattr(specific, trans_field_name):
        value = getattr(specific, trans_field_name)
    else:
        value = getattr(specific, field)

    return value or getattr(specific, field)
#
#
# class TransFieldNode(Node):
#     def __init__(self, filter_expression, asvar=None):
#         self.asvar = asvar
#         self.filter_expression = filter_expression
#         if isinstance(self.filter_expression.var, six.string_types):
#             self.filter_expression.var = Variable("'%s'" %
#                                                   self.filter_expression.var)
#
#     def render(self, context):
#         output = self.filter_expression.resolve(context)
#         value = render_value_in_context(output, context)
#         if self.asvar:
#             context[self.asvar] = value
#             return ''
#         else:
#             return value

#
# @register.tag
# def trans_field(parser, token):
#
#     args = token.contents.split()
#     if len(args) != 3 or args[1] != 'as':
#         pass
#     return TransFieldNode(args[0])
#
#     lang_code = translation.get_language()
#     trans_field_name = '%s_%s' % (field, lang_code)
#     specific = instance.specific if isinstance(instance, Page) else instance
#     if hasattr(specific, trans_field_name):
#         value = getattr(specific, trans_field_name)
#     else:
#         value = getattr(specific, field)
#
#     return value if value is not None else ''



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


