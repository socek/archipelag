from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from archipelag.event.forms import EventForm


@login_required
def register_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/market/')
    else:
        form = EventForm()
    return render(request, 'registration/event.html', {'form': form})
