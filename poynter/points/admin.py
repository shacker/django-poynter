from django.contrib import admin
from .forms import TicketForm
from .models import Space, Ticket, Vote, Project


class VoteAdmin(admin.ModelAdmin):
    list_display = ("created", "vote")

class TicketAdmin(admin.ModelAdmin):
    form = TicketForm
    list_display = ("title", "active", "pointing_session", "created")

class SpaceAdmin(admin.ModelAdmin):
    list_display = ("project", "moderator")


admin.site.register(Vote, VoteAdmin)
admin.site.register(Space, SpaceAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Project)
