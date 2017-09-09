from django.conf.urls import url
from archipelag.event.views import register_event

urlpatterns = [
    url(r'^register/', register_event)
]