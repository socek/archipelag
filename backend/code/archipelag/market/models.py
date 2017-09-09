from django.db import models
from archipelag.event.models import Event


class Market(models.Model):
    event = models.OneToOneField(Event)
    added_at = models.DateTimeField(auto_now_add=True)

