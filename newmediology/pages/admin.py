from django.contrib import admin

from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'visible')
    list_editable = ('visible',)

admin.site.register(Page, PageAdmin)
