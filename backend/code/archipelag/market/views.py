from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from json import loads
from datetime import datetime
from archipelag.market.models import Market
from django.shortcuts import redirect

class MarketView(LoginRequiredMixin, View):
    template_name = 'market/list.html'

    def get(self, request):
        return render(
            request, self.template_name,
            {
                'user_messages': Market.objects.all(),
            })


@login_required
def market_create(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = loads(body_unicode)

        new_market = Market.objects.create(
            owner=request.user.ngouser,
            title=body_data["title"],
            url=body_data["url"],
            date_starting=body_data["dateFrom"],
            date_ending=body_data["dateTo"],
            hashtag = body_data["hashtag"]
        )

        return HttpResponseRedirect(reverse('message_create', kwargs={'market_id':new_market.id}))
    return render(request, 'registration/event.html', )
