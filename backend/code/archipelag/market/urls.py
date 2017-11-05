from django.conf.urls import url

from archipelag.market.views import MarketView
from archipelag.market.views import market_create

urlpatterns = [
    url(r'^$', MarketView.as_view(), name="market"),
    url(r'^create/', market_create, name="create")
]