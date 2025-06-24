from django.contrib import admin
from .models import Vote, PointingSession, Ticket
from poynter.points.models import Profile





class VoteAdmin(admin.ModelAdmin):
    list_display = ("profile", "log_date", "vote")

class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "pointing_session", "created")


admin.site.register(Vote, VoteAdmin)
admin.site.register(Profile)
admin.site.register(PointingSession)
admin.site.register(Ticket, TicketAdmin)
