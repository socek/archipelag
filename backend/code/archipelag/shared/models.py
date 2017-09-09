from archipelag.ngo.models import NgoUser
from archipelag.market.models import Market
from django.db.models import CharField
from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import DateField

CATEGORIES = (
    ('FB', 'Facebook'),
    ('IP', 'Informacja Prasowa'),
    ('NEWS', 'Newsletter'),
    ('INST', 'Instagram'),
    ('TW', 'Twitter'),
    ('SMS', 'SMS Kiss'),
)


class Shared(Model):
    category = CharField(max_length=4, choices=CATEGORIES, default='FB')
    who_shared = ForeignKey(NgoUser)
    date_shared = DateField(null=False)
    visible_event = ForeignKey(Market)
