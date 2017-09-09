from archipelag.market.models import Market
from django.contrib.admin import ModelAdmin
from django.contrib.admin import site


class MarketAdmin(ModelAdmin):
    pass

site.register(Market, MarketAdmin)
