from django.forms import ModelForm

from archipelag.event.models import Event


class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = [
            'title',
            'url',
            'text',
            'date_starting',
            'date_ending']
