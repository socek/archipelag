from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from archipelag.message.forms import MessageForm
from archipelag.message.models import Message
from archipelag.market.models import Market

#from archipelag.notification.tasks import send_notification_for_event

from archipelag.market.settings import POINTS_RULES
from archipelag.ngo.models import NgoUser

@login_required
def message_create(request, market_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            market = Market.objects.get(id=market_id)
            event.market = market
            event.save()
            #send_notification_for_event.delay(event.id)
            form = MessageForm()
            service_name = event.type.service
            msg_for_user = "Twoja wiadomość na {} została dodana, dodaj wiadomości na inne platformy".format(service_name)
            add_coins_if_rules_allow(request.user.ngouser, market_id)
            return render(request, 'registration/message.html', {'form': form, 'message':msg_for_user})
    else:
        form = MessageForm()
    return render(request, 'registration/message.html', {'form': form})


def add_coins_if_rules_allow(ngo, market_id):
    messages = Message.objects.filter(market_id=market_id).count()
    if messages > 3:
        coins_to_add = POINTS_RULES['create_more_than_three_messages_format']
        ngo_model = NgoUser()
        ngo_model.add_coins(ngo, coins_to_add)


def add_point(request, market_id):
    current_ngo = request.user.ngouser
    ngo_model = NgoUser()
    ngo_model.add_coins(current_ngo, POINTS_RULES['for_share'])
    current_ngo.save()
    return redirect('market_details', market_id=market_id)
