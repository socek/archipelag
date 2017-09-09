from django.conf.urls import url

from archipelag.market.views import Market


urlpatterns = [
    url(r'^$', Market.as_view(), name="market"),
]
