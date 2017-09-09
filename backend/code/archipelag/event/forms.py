from django import forms
from datetime import datetime

class EventForm(forms.Form):
    title = forms.CharField(label='Tytul', max_length=120)
    url = forms.URLField(label='Link', required=False)
    date_starting = forms.DateTimeField(label='Czas rozpoczecia', initial=datetime.now)
    date_ending = forms.DateTimeField(label='Czas zakonczenia', initial=datetime.now)
    text = forms.CharField(label='Tresc', required=True)
