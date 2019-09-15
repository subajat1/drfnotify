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
        'head_payload',
        'body_payload',
        'url_payload',
    )
    search_fields = ('head_payload', 'body_payload', 'url_payload')

admin.site.register(models.Message, MessageAdmin)


