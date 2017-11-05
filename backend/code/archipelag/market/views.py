from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from archipelag.market.models import Market
from archipelag.market.forms import MarketForm
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
        form = MarketForm(request.POST)
        if form.is_valid():
            market = form.save(commit=False)
            market.owner = request.user.ngouser
            market.save()
            return redirect('/message/create/%s' % market.id)
    else:
        form = MarketForm()
    return render(request, 'registration/event.html', {'form': form})
