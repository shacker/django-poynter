from django.urls import path
from poynter.points import views
from poynter.points.models import Vote

home_list_view = views.HomeListView.as_view(
    queryset=Vote.objects.order_by("-created")[:5],  # :5 limits the results to the five most recent
    context_object_name="vote_list",
    template_name="points/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("vote/", views.vote, name="vote"),

]

