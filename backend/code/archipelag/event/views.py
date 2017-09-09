from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from archipelag.event.forms import EventForm
from archipelag.notification.tasks import send_notification_for_event


@login_required
def register_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user.ngouser
            event.save()
            send_notification_for_event.delay(event.id)
            return HttpResponseRedirect('/market/')
    else:
        form = EventForm()
    return render(request, 'registration/event.html', {'form': form})
