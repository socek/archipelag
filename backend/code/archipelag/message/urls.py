from django.conf.urls import url
from archipelag.message.views import message_create

urlpatterns = [
    url(r'^create/(?P<market_id>\d+)/$', message_create, name="message_create")
]
