from django.db import models
from archipelag.ngo.models import NgoUser
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=120, blank=True, null=False)
    url = models.URLField(null=True)
    date_starting = models.DateField()
    date_ending = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    shares = models.PositiveIntegerField()
    owner = models.ForeignKey(NgoUser)

