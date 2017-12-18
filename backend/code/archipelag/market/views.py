from json import loads

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from archipelag.market.settings import POINTS_RULES
from archipelag.market.models import Market
from archipelag.market.forms import MarketForm
from archipelag.message.models import Message
from archipelag.event.models import Event


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
    if request.method != 'POST':
        return render(request, 'registration/event.html')

    body_data = loads(request.body.decode('utf-8'))
    if not is_fields_are_valid(body_data):
        error = dict(error="Błędny url.")
        return JsonResponse(error)
    current_ngo = request.user.ngouser
    if current_ngo.is_user_can_add_market():
        current_ngo.subtract_coins(POINTS_RULES['add_own_market'])
        new_market = get_new_market(current_ngo, body_data)
        message_create_url = reverse('message_create', args=[new_market.id,])
        return JsonResponse(dict(url=message_create_url))
    else:
        error = dict(error="Za mało punktów.")
        return JsonResponse(error)


def is_fields_are_valid(fields):
    forms = MarketForm(data=fields)
    return forms.is_valid()


def get_new_market(current_ngo, body_data):
    new_market = Market.objects.create(
        owner=current_ngo,
        title=body_data["title"],
        url=body_data["url"],
        date_starting=body_data["date_starting"],
        date_ending=body_data["date_ending"],
        hashtag=body_data["hashtag"]
    )
    return new_market


def get_messages(request, market_id):

    market = Market.objects.filter(id=market_id)
    messages = Message.objects.filter(market=market_id).all()
    logs = []


    template_name = 'market/message_list.html'
    return render(
            request, template_name,
            {
                'messages': Message.objects.filter(market=market).all(),
                'logs': get_logs(messages)
            })


def get_logs(messages):
    for message in messages:
        events = Event.objects.filter(id_connected_object=message.id).all()
        if events:
            for event in events:
                date_created = event.date_created.strftime("%Y-%m-%d %H:%M")
                yield "Użytkownik {} udostępnił na {} dnia {}".format(event.owner, message.type, date_created)
