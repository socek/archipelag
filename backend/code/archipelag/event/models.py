from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import AutoField

from django.contrib.postgres.fields import JSONField


from archipelag.ngo.models import NgoUser


class EventType(Model):
    TYPES = (
        ('SH', 'SHARE'),
        ('AP', 'ADMIN PROMOTE'),
        ('RI', 'REGISTER FROM INVITATION'),
        ('R', 'REGISTER'),
    )
    type_id = AutoField(primary_key=True)
    name = CharField(max_length=4, choices=TYPES)


class Event(Model):
    owner = ForeignKey(NgoUser, null=False)
    type = ForeignKey(EventType, null=False)
    date_created = DateTimeField(auto_now_add=True)
    content = JSONField(null=False)

