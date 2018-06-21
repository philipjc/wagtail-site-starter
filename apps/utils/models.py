from django.db import models

# Wagtail
from wagtail.core.models import Page
from wagtail.core.blocks import ListBlock, ChoiceBlock, TextBlock, StructBlock, StreamBlock, CharBlock, \
    RichTextBlock, BooleanBlock, URLBlock, PageChooserBlock


# Create your models here.
class BasePage(Page):
    # Page Header
    page_title = models.CharField(max_length=200, blank=True, verbose_name='Title',
                                  help_text="Optional. If nothing is entered, the page title will be used.")
    page_header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Page Header image'
    )

    class Meta:
        abstract = True


# Steamfields

# Blocks
class TwoColumnBlock(StructBlock):

    title = CharBlock(required=False, help_text='Optional.')
    left_column = RichTextBlock(required=False)
    right_column = RichTextBlock(required=False)


class ThreeColumnBlock(StructBlock):

    title = CharBlock(required=False, help_text='Optional.')
    left_column = RichTextBlock(required=False)
    middle_column = RichTextBlock(required=False)
    right_column = RichTextBlock(required=False)


class ContentBlock(StructBlock):

    content = RichTextBlock()


class QuoteBlock(StructBlock):

    quote_text = TextBlock()
    name = CharBlock(required=False)
    job_title = CharBlock(required=False)
    company_name = CharBlock(required=False)


class VideoBlock(StructBlock):

    url = URLBlock()


class CalloutBlock(StructBlock):

    content = RichTextBlock()


# Streamfield Model

class GeneralStreamBlock(StreamBlock):

    content = ContentBlock(icon="pilcrow", label="Single Column")
    two_columns = TwoColumnBlock(icon="pilcrow", label='Two Columns')
    three_columns = ThreeColumnBlock(icon="pilcrow", label='Three Columns')
    quote = QuoteBlock(icon="openquote", label='Quote')
    video = VideoBlock(icon="media", label='Video')
    callout = CalloutBlock(icon="placeholder", label="Callout")


class DetailPageStreamBlock(StreamBlock):

    content = ContentBlock(icon="pilcrow", label="Single Column")
    two_columns = TwoColumnBlock(icon="pilcrow", label='Two Columns')
    video = VideoBlock(icon="media", label='Video')
    quote = QuoteBlock(icon="openquote", label='Quote')