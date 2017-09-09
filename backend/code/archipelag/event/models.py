from django.db.models import CharField
from django.db.models import DateField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import PositiveIntegerField
from django.db.models import TextField
from django.db.models import URLField

from archipelag.ngo.models import NgoUser


class Event(Model):
    title = CharField(max_length=120, blank=True, null=False)
    url = URLField(null=True)
    date_starting = DateField(null=True, blank=True)
    date_ending = DateField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)
    shares = PositiveIntegerField(null=True, blank=True)
    text = TextField(max_length=2048, blank=True)
    owner = ForeignKey(NgoUser, null=False)
    hashtag = CharField(max_length=128, default='')
