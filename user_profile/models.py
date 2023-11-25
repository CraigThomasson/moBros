from django.db import models
from django.contrib.auth.models import User
from activities.models import Activity
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    activities = models.ManyToManyField(Activity, blank=True)
    fitness_level = models.IntegerField(default=1)
    mindfulness_level = models.IntegerField(default=1)

    # TODO: water intake tracker to be linked to user profile

    # Add other fields as necessary

    def __str__(self):
        return f"{self.user.username}'s Profile"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()