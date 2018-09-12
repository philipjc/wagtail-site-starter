from django.contrib import admin

# Register your models here.
from .models import NewsLetterSubscriber


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email', 'signup_date')


admin.site.register(NewsLetterSubscriber, NewsLetterAdmin)
