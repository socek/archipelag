from django.forms import ModelForm

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
