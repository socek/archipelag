from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import Model
from django.db.models import OneToOneField


class NgoUser(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    name = CharField(max_length=100)
