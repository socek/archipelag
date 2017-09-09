from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from archipelag.event.models import Event


class Market(LoginRequiredMixin, View):
    template_name = 'market/list.html'

    def get(self, request):
        return render(
            request, self.template_name,
            {
                'user_events': Event.objects.all(),
            })
