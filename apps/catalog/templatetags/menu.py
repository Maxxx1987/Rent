from django import template
from apps.catalog.models import Category

register = template.Library()


@register.inclusion_tag('menu.html')
def top_bar():
    return {
        'menu': Category.objects.prefetch_related('sections'),
    }
