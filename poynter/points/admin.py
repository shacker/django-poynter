from django.contrib import admin

from .models import PointingSession, Ticket, Vote


class VoteAdmin(admin.ModelAdmin):
    list_display = ("created", "vote")

class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "pointing_session", "created")

class PointingSessionAdmin(admin.ModelAdmin):
    list_display = ("moderator", "session_date", )


admin.site.register(Vote, VoteAdmin)
admin.site.register(PointingSession, PointingSessionAdmin)
admin.site.register(Ticket, TicketAdmin)
