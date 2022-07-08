from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.utils import timezone
# Create your views here.
from .models import Invite
from django.urls import reverse_lazy
now = timezone.now()


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invites = Invite.objects.all()
        context["invites"] = invites
        return context

    def post(self, request, *args, **kwargs):
        pk = request.POST.get("pk")
        invite = Invite.objects.get(id=pk)
        if "arrive" in request.POST:
            invite.arrived = True
            invite.time_of_arrival = now
        if "undo" in request.POST:
            invite.arrived = False
        invite.save()
        return redirect('taguy:index')


@csrf_exempt
def index(request):
    invites = Invite.objects.all()
    if request.method == 'POST':
        pk = request.POST.get("pk")
        invite = Invite.objects.get(id=pk)
        if "arrive" in request.POST:
            invite.arrived = True
            invite.time_of_arrival = now
        if "undo" in request.POST:
            invite.arrived = False
        invite.save()
        return redirect('taguy:index')
    return render(request, "index.html", {"invites": invites})
