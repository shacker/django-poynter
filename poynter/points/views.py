
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from poynter.points.forms import VoteForm
from poynter.points.models import Vote, Project
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    "List spaces - projects and their pointing moderators"
    projects = Project.objects.all()
    return render(request, "points/home.html", {"projects": projects})


def about(request):
    return render(request, "points/about.html")


@login_required
def vote(request):
    "Submit a vote - TODO show what we're voting on"
    form = VoteForm(request.POST or None)

    if request.method == "POST":
        message = form.save(commit=False)
        message.log_date = datetime.now()
        message.voter = request.user  # Associate the message with the logged-in user
        message.save()
        return redirect("points:votes")
    else:
        return render(request, "points/vote.html", {"form": form})

@login_required
def votes(request):
    "Filtered list of votes"
    votes = Vote.objects.all()
    return render(request, "points/votes.html", {"votes": votes})
