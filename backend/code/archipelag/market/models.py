from django.db import models
from archipelag.ngo.models import NgoUser
from archipelag.event.models import Event
# Create your models here.

CATEGORIES = (
    ('FB', 'Facebook'),
    ('IP', 'Informacja Prasowa'),
    ('NEWS', 'Newsletter'),
    ('INST', 'Instagram'),
    ('TW', 'Twitter'),
    ('SMS', 'SMS Kiss'),
)


class Market(models.Model):
    category = models.CharField(max_length=4, choices=CATEGORIES, default='FB')
    date_shared = models.DateField(null=False)
    who_shared = models.ForeignKey(NgoUser)
    hash_tag = models.CharField(max_length=120, null=False)
    event = models.ForeignKey(Event)
