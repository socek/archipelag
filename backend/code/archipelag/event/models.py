from django.db import models
from archipelag.ngo.models import NgoUser
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=120, blank=True, null=False)
    url = models.URLField(null=True)
    date_starting = models.DateField(null=True, blank=True)
    date_ending = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    shares = models.PositiveIntegerField(null=True, blank=True)
    text = models.TextField(max_length=2048, blank=True)
    owner = models.OneToOneField(NgoUser, null=True)
    hashtag = models.CharField(max_length=128, default='')
