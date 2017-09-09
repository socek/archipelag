from django.db import models
from archipelag.ngo.models import NgoUser
# Create your models here.

CATEGORIES = (
    ('FB', 'Facebook'),
    ('IP', 'Informacja Prasowa'),
    ('NEWS', 'Newsletter'),
    ('INST', 'Instagram'),
    ('TW', 'Twitter'),
    ('SMS', 'SMS Kiss'),
)

class Event(models.Model):
    title = models.CharField(max_length=120, blank=True, null=False)
    email = models.EmailField(null=False)
    category = models.CharField(max_length=4, choices=CATEGORIES, default='FB')
    url = models.URLField(null=True)
    date_starting = models.DateField()
    date_ending = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    shares = models.PositiveIntegerField()
    owner = models.ForeignKey(NgoUser)


class Shared(models.Model):
    category = models.CharField(max_length=4, choices=CATEGORIES, default='FB')
    date_shared = models.DateField()
    who_shared = models.ForeignKey(NgoUser)
    hash_tag = models.CharField(max_length=120, null=False)
