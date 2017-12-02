from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import Model
from django.db.models import OneToOneField
from django.db.models import PositiveIntegerField


class NgoUser(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    name = CharField(max_length=100)
    coins = PositiveIntegerField(default=0)
    fb_token = CharField(max_length=256, blank=True)
    twitter_token = CharField(max_length=256, blank=True)

    def __str__(self):
        return str(self.user)

