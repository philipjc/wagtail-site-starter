# Generated by Django 2.0.5 on 2018-06-21 16:35

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0020_add-verbose-name'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('page_title', models.CharField(blank=True, help_text='Optional. If nothing is entered, the page title will be used.', max_length=200, verbose_name='Title')),
                ('body', wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())], icon='pilcrow', label='Single Column')), ('two_columns', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Optional.', required=False)), ('left_column', wagtail.core.blocks.RichTextBlock(required=False)), ('right_column', wagtail.core.blocks.RichTextBlock(required=False))], icon='pilcrow', label='Two Columns')), ('three_columns', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Optional.', required=False)), ('left_column', wagtail.core.blocks.RichTextBlock(required=False)), ('middle_column', wagtail.core.blocks.RichTextBlock(required=False)), ('right_column', wagtail.core.blocks.RichTextBlock(required=False))], icon='pilcrow', label='Three Columns')), ('quote', wagtail.core.blocks.StructBlock([('quote_text', wagtail.core.blocks.TextBlock()), ('name', wagtail.core.blocks.CharBlock(required=False)), ('job_title', wagtail.core.blocks.CharBlock(required=False)), ('company_name', wagtail.core.blocks.CharBlock(required=False))], icon='openquote', label='Quote')), ('video', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock())], icon='media', label='Video')), ('callout', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())], icon='placeholder', label='Callout'))], blank=True)),
                ('page_header_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Page Header image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('page_title', models.CharField(blank=True, help_text='Optional. If nothing is entered, the page title will be used.', max_length=200, verbose_name='Title')),
                ('body', wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())], icon='pilcrow', label='Single Column')), ('two_columns', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Optional.', required=False)), ('left_column', wagtail.core.blocks.RichTextBlock(required=False)), ('right_column', wagtail.core.blocks.RichTextBlock(required=False))], icon='pilcrow', label='Two Columns')), ('three_columns', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Optional.', required=False)), ('left_column', wagtail.core.blocks.RichTextBlock(required=False)), ('middle_column', wagtail.core.blocks.RichTextBlock(required=False)), ('right_column', wagtail.core.blocks.RichTextBlock(required=False))], icon='pilcrow', label='Three Columns')), ('quote', wagtail.core.blocks.StructBlock([('quote_text', wagtail.core.blocks.TextBlock()), ('name', wagtail.core.blocks.CharBlock(required=False)), ('job_title', wagtail.core.blocks.CharBlock(required=False)), ('company_name', wagtail.core.blocks.CharBlock(required=False))], icon='openquote', label='Quote')), ('video', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock())], icon='media', label='Video')), ('callout', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())], icon='placeholder', label='Callout'))], blank=True)),
                ('page_header_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Page Header image')),
            ],
            options={
                'verbose_name': 'Home',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RedirectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('alias_for_page', models.ForeignKey(blank=True, help_text="If an alias isn't selected then this page will redirect to it's first child", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
