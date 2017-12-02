from django.forms import ModelForm
from django.forms import DateTimeInput

from archipelag.market.models import Market


class MarketForm(ModelForm):

    class Meta:
        model = Market
        exclude = ["owner"]
        fields = [
            'title',
            'url',
            'date_starting',
            'date_ending',
            'hashtag']
        widgets = {
            'date_starting': DateTimeInput(attrs={'class': 'date_starting'}),
            'date_ending': DateTimeInput(attrs={'class': 'date_ending'})
        }
