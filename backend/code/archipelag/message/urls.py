from django.conf.urls import url
from archipelag.message.views import message_create
from archipelag.message.views import add_point

urlpatterns = [
    url(r'^create/(?P<market_id>\d+)/$', message_create, name="message_create"),
    url(r'^add_point/(?P<market_id>\d+)/$', add_point, name='user_add_point'),
]
