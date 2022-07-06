from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .models import Invite


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invites = Invite.objects.all()
        context["invites"] = invites
        return context
