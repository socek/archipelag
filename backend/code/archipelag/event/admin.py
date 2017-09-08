from django.contrib import admin
from archipelag.event.models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
