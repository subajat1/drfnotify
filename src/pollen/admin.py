from django.contrib import admin

from . import models

class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sender',
        'receiver',
        'head',
    )
    search_fields = ('name', 'head', 'body', 'url')

admin.site.register(models.Content, ContentAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'content',
        'head_data',
        'body_data',
        'url_data',
    )
    search_fields = ('head_data', 'body_data', 'url_data')

admin.site.register(models.Message, MessageAdmin)


