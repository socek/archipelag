from django.db.models import BooleanField
from django.db.models import Model
from django.db.models import OneToOneField

from archipelag.event.models import Event
from archipelag.ngo.models import NgoUser


class Notification(Model):
    owner = OneToOneField(NgoUser)
    event = OneToOneField(Event)
    sent = BooleanField(default=False, null=False)
