from django import template
from wagtail.core.models import Page

register = template.Library()


@register.inclusion_tag('partials/menu.html')
def menu():

    pages = Page.objects.all().live().in_menu()

    return {
        'pages': pages,
    }
