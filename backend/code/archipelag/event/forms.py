from django import forms
from datetime import datetime

class EventForm(forms.Form):
    title = forms.CharField(label='tytul', max_length=120)
    url = forms.URLField(label='link', required=False)
    date_starting = forms.DateField(label='Czas rozpoczecia', initial=datetime.now)
    date_ending = forms.DateField(label='Czas zakonczenia', initial=datetime.now)
    text = forms.CharField(label='tresc', required=True)
