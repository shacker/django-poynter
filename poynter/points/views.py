import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from poynter.points.forms import LogMessageForm
from poynter.points.models import LogMessage
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "points/about.html")


@login_required
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        message = form.save(commit=False)
        message.log_date = datetime.now()
        message.profile = request.user.profile  # Associate the message with the logged-in user
        message.save()
        return redirect("home")
    else:
        return render(request, "points/log_message.html", {"form": form})
