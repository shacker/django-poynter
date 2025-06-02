from django.contrib import admin
from .models import LogMessage
from poynter.points.models import Profile





class LogMessageAdmin(admin.ModelAdmin):
    list_display = ("profile", "log_date", "message")



admin.site.register(LogMessage, LogMessageAdmin)
admin.site.register(Profile)
