from django.db import models
from django.db.models import ForeignKey
from django.db.models import TextField
from django.db.models import URLField
from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import PositiveIntegerField

from archipelag.market.models import Market


class MessageType(models.Model):
    CATEGORIES = (
        ('FB', 'Facebook'),
        ('IP', 'Informacja Prasowa'),
        ('NEWS', 'Newsletter'),
        ('INST', 'Instagram'),
        ('TW', 'Twitter'),
        ('SMS', 'SMS Kiss'),
    )
    service = CharField(max_length=4, choices=CATEGORIES, default='FB')
    count_hashtag = BooleanField(default=True, blank=True)
    char_restriction = PositiveIntegerField(null=False, blank=True)


class Message(models.Model):
    content = TextField(max_length=2048, blank=True)
    shared = URLField(null=True)
    type = ForeignKey(MessageType, null=False)
    market = ForeignKey(Market, null=False)
