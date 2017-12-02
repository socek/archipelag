from django.contrib import admin
from archipelag.event.models import Event
from archipelag.event.models import EventType

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventAdmin)
