from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a string representation of a message."""
        return f"{self.user.username}"

class LogMessage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


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
