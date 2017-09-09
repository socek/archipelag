from django.shortcuts import render
from django.http import HttpResponseRedirect
from archipelag.event.forms import EventForm
# Create your views here.

def register_event(request):
    if request.method == 'POST':
        form = EventForm(request.PO)
        if form.is_valid():
            return HttpResponseRedirect('/success/')
    else:
        form = EventForm()
    return render(request, 'registration/event.html', {'form': form})

