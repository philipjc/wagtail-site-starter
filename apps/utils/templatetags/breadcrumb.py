from django import template
from wagtail.core.models import Page

register = template.Library()


@register.inclusion_tag('partials/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):

    self = context.get('self')

    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }
