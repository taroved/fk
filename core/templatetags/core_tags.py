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


