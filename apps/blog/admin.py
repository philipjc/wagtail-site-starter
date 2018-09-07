from django.contrib import admin
from django import forms

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from .models import BlogIndexPage, BlogPage, BlogPageGalleryImage, BlogCategory

# Register your models here.

BlogIndexPage.content_panels = BlogIndexPage.content_panels + [
    FieldPanel('intro', classname="full")
]

BlogPage.content_panels = BlogPage.content_panels + [

    MultiFieldPanel([
        FieldPanel('date'),
        FieldPanel('tags'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ], heading="Blog information"),
    FieldPanel('intro'),
    FieldPanel('body'),
    InlinePanel('gallery_images', label="Gallery images"),
]

BlogPageGalleryImage.panels = [
    ImageChooserPanel('image'),
    FieldPanel('caption'),
]

BlogCategory.panels = [
    FieldPanel('name'),
    ImageChooserPanel('icon'),
]
