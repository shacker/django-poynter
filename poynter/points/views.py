
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from poynter.points.forms import VoteForm
from poynter.points.models import Vote
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Vote

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "points/about.html")


@login_required
def vote(request):
    form = VoteForm(request.POST or None)

    if request.method == "POST":
        message = form.save(commit=False)
        message.log_date = datetime.now()
        message.voter = request.user  # Associate the message with the logged-in user
        message.save()
        return redirect("home")
    else:
        return render(request, "points/vote.html", {"form": form})
