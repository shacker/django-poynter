from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



@login_required
@csrf_exempt  # For demo purposes - use proper CSRF handling in production
def tally_single(request):
    """HTMX view receives POST from a voting space, and logs
    the space name, username, and vote.


    space_key = {

    }
    """
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        vote = data.get("number")
        space = data.get("space")
        ticket = data.get("ticket")

        space_key = f"{space}_{username}_{ticket}"
        value = {
            "space": space,
            "username": username,
            "ticket": ticket,
            "vote": vote
        }

    # TODO: Store dict in redis for later retrieval...

    return HttpResponse("Nothing")


