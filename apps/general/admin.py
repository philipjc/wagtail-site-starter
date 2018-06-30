from django.contrib import admin

# Wagtail
from wagtail.core.models import Page

# from wagtail.admin.blocks import
# from wagtail.images.blocks import
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

# Apps
from .models import HomePage

# Register your models here.
HomePage.content_panels = HomePage.content_panels + [
    StreamFieldPanel('body'),
]
