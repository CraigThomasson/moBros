from django.db import models

from activities.models import Exercise


# Create your models here.
class Profile(models.Model):
    exercises = models.ForeignKey(Exercise, on_delete=models.CASCADE)
