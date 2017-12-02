from django.conf.urls import url

from archipelag.market.views import MarketView
from archipelag.market.views import market_create
from archipelag.market.views import get_messages
from archipelag.market.views import add_point

urlpatterns = [
    url(r'^$', MarketView.as_view(), name="market"),
    url(r'^create/', market_create, name="create"),
    url(r'^details/(?P<market_id>\d+)/$', get_messages, name='market_details'),
    url(r'^add_point/(?P<market_id>\d+)/$', add_point, name='user_add_point'),

]