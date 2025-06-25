from django.urls import path
from poynter.points import views

app_name = "points"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("votes/", views.votes, name="votes"),
    path("vote/", views.vote, name="vote"),
    path("space/<str:slug>", views.space, name="space"),


]

