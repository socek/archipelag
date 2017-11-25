from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from archipelag.message.forms import MessageForm
from archipelag.market.models import Market
#from archipelag.notification.tasks import send_notification_for_event
from django.shortcuts import render_to_response

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
            return HttpResponseRedirect('/market/')
    else:

        return render_to_response(request, 'registration/message.html')