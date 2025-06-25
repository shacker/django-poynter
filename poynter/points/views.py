from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import datetime

from poynter.points.forms import VoteForm
from poynter.points.models import Project, Space, Ticket, Vote


@login_required
def home(request):
    "List spaces - projects and their pointing moderators"
    projects = Project.objects.all()
    open_spaces = Space.objects.filter(is_open=True)
    return render(request, "points/home.html", {"projects": projects, "open_spaces": open_spaces})

@login_required
def space(request, slug: str):
    "Detail view for a voting space has permanent URL for a moderator and project."
    space = get_object_or_404(Space, slug=slug)

    # try/except
    active_ticket = space.ticket_set.get(active=True)


    return render(request, "points/space.html", {"space": space, "active_ticket": active_ticket})


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



