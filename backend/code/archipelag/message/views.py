from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from archipelag.message.forms import MessageForm
from archipelag.market.models import Market
#from archipelag.notification.tasks import send_notification_for_event


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
            return render(request, 'registration/message.html', {'form': form, 'message':msg_for_user})
    else:
        form = MessageForm()
    return render(request, 'registration/message.html', {'form': form})