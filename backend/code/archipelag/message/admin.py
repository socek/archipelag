from django.contrib.admin import ModelAdmin
from django.contrib.admin import site

from archipelag.message.models import Message
from archipelag.message.models import MessageType

class MessageAdmin(ModelAdmin):
    pass

site.register(Message, MessageAdmin)
site.register(MessageType, MessageAdmin)
