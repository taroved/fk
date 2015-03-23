# coding=utf-8
from datetime import date
from django import template
from django.template import Node, Variable
from django.template.base import render_value_in_context
from django.utils import translation
import six
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin
from wagtail.contrib.wagtailroutablepage.templatetags.wagtailroutablepage_tags import routablepageurl
from wagtail.wagtailcore.models import Page
from core.models import SliderItem, Partner, OrganizerPage, NewsIndexPage

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

    # if has_ru or has_en field is set to false immediately return empty string
    # but always use title it's not title
    # if field != 'title' and hasattr(specific, 'has_'+lang_code) and not getattr(specific, 'has_'+lang_code, False):
    #     return ''

    if hasattr(specific, trans_field_name):
        value = getattr(specific, trans_field_name)
    else:
        value = getattr(specific, field)

    return value or ''


@register.simple_tag
def list_index(lst, index):
    print lst, index
    return lst[index]


@register.assignment_tag
def assign(value):
    return value


@register.filter
def split(str, splitter):
    return str.split(splitter)

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


def has_translation(page, lang):
    if lang == 'uk':
        return True
    specific = page.specific
    return bool(getattr(specific, 'title_'+lang).strip())


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return issubclass(page.specific_class, RoutablePageMixin) or page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
@register.inclusion_tag('core/tags/top_menu.html', takes_context=True)
def top_menu(context, parent=None, calling_page=None):
    request = context['request']
    # menuitems = parent.get_children().live().in_menu()
    if not parent:
        parent = context['request'].site.root_page
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


@register.inclusion_tag('core/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    is_routable = issubclass(parent.specific_class, RoutablePageMixin)
    if is_routable:
        menuitems_children = parent.specific.construct_menu()
    else:
        menuitems_children = parent.get_children()
        menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent if not is_routable else parent.specific,
        'parent_is_routable': is_routable,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the bottom menu items - the immediate children of the parent page
@register.inclusion_tag('core/tags/bottom_menu.html', takes_context=True)
def bottom_menu(context, parent=None, calling_page=None):
    request = context['request']
    if not parent:
        parent = context['request'].site.root_page
    menuitems = parent.get_children().live().in_menu().not_type(NewsIndexPage)
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


@register.inclusion_tag('core/tags/bottom_menu_children.html', takes_context=True)
def bottom_menu_children(context, parent):
    return top_menu_children(context, parent)
