from os import environ

from celery import Celery
from django.conf import settings


environ.setdefault('DJANGO_SETTINGS_MODULE', 'archipelag.app.settings')
capp = Celery('archipelag')
capp.config_from_object('django.conf:settings', namespace='CELERY')
capp.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
