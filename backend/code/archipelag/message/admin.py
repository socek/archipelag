from django.contrib.admin import ModelAdmin
from django.contrib.admin import site

from archipelag.message.models import Message

class MessageAdmin(ModelAdmin):
    pass

site.register(Message, MessageAdmin)
