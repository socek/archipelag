from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from json import loads
from archipelag.market.models import Market
from archipelag.message.models import Message
from django.http import JsonResponse
from django.shortcuts import redirect


POINTS_RULES = dict(
    for_share=2,
    share_more_than_three=0.5,
    create_more_than_three_messages_format=0.5,
    share_more_than_three_messages_format=0.5,)


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
            date_starting=body_data["date_starting"],
            date_ending=body_data["date_ending"],
            hashtag = body_data["hashtag"]
        )
        data = dict(url='/message/create/%s'%new_market.id)
        return JsonResponse(data)
    return render(request, 'registration/event.html', )


def get_messages(request, market_id):
    market = Market.objects.filter(id=market_id)
    template_name = 'market/message_list.html'
    return render(
            request, template_name,
            {
                'messages': Message.objects.filter(market=market).all(),
            })


def add_point(request, market_id):
    from archipelag.ngo.models import NgoUser
    current_ngo = request.user.ngouser
    ngo_model = NgoUser()
    ngo_model.add_coins(current_ngo, POINTS_RULES['for_share'])
    current_ngo.save()
    return redirect('market_details', market_id=market_id)