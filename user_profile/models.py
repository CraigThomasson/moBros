from django.db import models
from django.contrib.auth.models import User
from activities.models import Exercise

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    exercises = models.ManyToManyField(Exercise, blank=True)
    fitness_level = models.IntegerField(default=1)
    mindfulness_level = models.IntegerField(default=1)
    # Add other fields as necessary

    def __str__(self):
        return f"{self.user.username}'s Profile"