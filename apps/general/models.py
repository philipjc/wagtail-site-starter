from django.db import models
from django.shortcuts import redirect

from modelcluster.fields import ParentalKey, ParentalManyToManyField

# Wagtail
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.search import index

# Apps
from ..utils.models import BasePage, GeneralStreamBlock

# Packages
from itertools import chain


# HOME PAGE
class HomePage(BasePage):

    class Meta:
        verbose_name = "Home"

    body = StreamField(GeneralStreamBlock, blank=True)

    search_fields = BasePage.search_fields + [
        index.SearchField('body', partial_match=True),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request)

        # content

        return context


# CONTENT PAGE
class ContentPage(BasePage, index.Indexed):

    body = StreamField(GeneralStreamBlock, blank=True)

    search_fields = BasePage.search_fields + [
        index.SearchField('body', partial_match=True),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(ContentPage, self).get_context(request)

        # content

        return context


# REDIRECT PAGE
class RedirectPage(Page):

    alias_for_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='redirects',
        help_text="If an alias isn't selected then this page will redirect to it's first child"
    )

    def serve(self, request):
        # Get the first child of this page
        first_child = self.get_children().live().in_menu().first()

        if self.alias_for_page:
            return redirect(self.alias_for_page.url, permanent=False)

        elif first_child:
            return redirect(first_child.url, permanent=False)
