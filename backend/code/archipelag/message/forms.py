from django.forms import ModelForm

from archipelag.message.models import Message


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = [
            'content',
            'type',]