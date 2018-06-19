
from django import template

register = template.Library()


@register.inclusion_tag('partials/footer.html')
def footer():

    return {

    }
