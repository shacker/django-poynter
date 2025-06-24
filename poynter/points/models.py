from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django_extensions.db.models import TimeStampedModel
import requests


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


class Vote(TimeStampedModel):
    """ One user votes on one issue"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    vote = models.SmallIntegerField(help_text="Numerical vote up to 2 digits")
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class PointingSession(TimeStampedModel):
    """ A session is a meeting in which users vote on stories.
    A PointingSession has a moderator and a collection of stories.
    TODO: Allow NOW or arbitrary date
    """
    moderator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    session_date = models.DateTimeField("date logged")

    def __str__(self):
        return f"{self.moderator.user.username}: {self.session_date.strftime('%A, %d %B, %Y at %X')}"


class Ticket(TimeStampedModel):
    """ A ticket reference (e.g. to Jira), to be stored in a PointingSession and voted on by users. """
    url = models.URLField(help_text="Link into ticket system", verbose_name="URL")
    title = models.name = models.CharField(max_length=120, blank=True, help_text="Extracted automatically if possible, or populate manually.")
    pointing_session = models.ForeignKey(PointingSession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}: {self.title}"


    def save(self, *args, **kwargs):
        """Try to populate the title automatically. If we can't get to the remote system,
        we can still enter the title manually. """
        if not self.title:
            headers = {}  # Need this?
            page = requests.get(self.url, headers=headers)
            text = page.text
            self.title = text[text.find('<title>') + 7 : text.find('</title>')]
        return super(Ticket, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """When new User is created, automatically create a corresponding Profile."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """When User is saved, also save their Profile.
    If user has no Profile (which should never happen),
    make one!"""

    if hasattr(instance, "profile"):
        instance.profile.save()
    else:
        Profile.objects.create(user=instance)
