import requests
from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel



class Project(TimeStampedModel):
    """Voting Sessions are associated with projects within the organization."""

    name = models.name = models.CharField(
        max_length=120,
        help_text="A project title within the organization.",
    )

    def __str__(self):
        return f"{self.name}"

class Vote(TimeStampedModel):
    """One user's vote on one ticket."""
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(help_text="Numerical vote up to 2 digits")

    def __str__(self):
        return f"'{self.voter}' on {self.created.strftime('%A, %d %B, %Y at %X')}"


class PointingSession(TimeStampedModel):
    """A session is a meeting in which users vote on stories.
    A PointingSession has a moderator and a collection of stories.
    TODO: Allow NOW or arbitrary date
    """

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    moderator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_date = models.DateTimeField("Voting window")
    is_open = models.BooleanField(help_text="Voting is currently open", default=False)

    def __str__(self):
        return f"{self.moderator.username}: {self.session_date.strftime('%A, %d %B, %Y at %X')}"

    class Meta:
        verbose_name = "Voting Session"
        verbose_name_plural = "Voting Sessions"


class Ticket(TimeStampedModel):
    """A ticket reference (e.g. to Jira), to be stored in a PointingSession and voted upon by users."""

    url = models.URLField(help_text="Link into ticket system", verbose_name="URL")
    title = models.name = models.CharField(
        max_length=120,
        blank=True,
        help_text="Extracted automatically if possible, or populate manually.",
    )
    pointing_session = models.ForeignKey(PointingSession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}: {self.title}"

    def save(self, *args, **kwargs):
        """Try to populate the title automatically. If we can't get to the remote system,
        we can still enter the title manually."""
        if not self.title:
            page = requests.get(self.url)
            text = page.text
            self.title = text[text.find("<title>") + 7 : text.find("</title>")]
        return super(Ticket, self).save(*args, **kwargs)
