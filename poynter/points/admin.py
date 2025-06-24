from django.contrib import admin
from .forms import TicketForm
from .models import PointingSession, Ticket, Vote, Project


class VoteAdmin(admin.ModelAdmin):
    list_display = ("created", "vote")

class TicketAdmin(admin.ModelAdmin):
    form = TicketForm
    list_display = ("title", "active", "pointing_session", "created")

class PointingSessionAdmin(admin.ModelAdmin):
    list_display = ("moderator", "project", "session_date", )


admin.site.register(Vote, VoteAdmin)
admin.site.register(PointingSession, PointingSessionAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Project)
