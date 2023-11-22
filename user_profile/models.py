from django.db import models
from django.contrib.auth.models import User

from activities.models import Exercise


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exercises = models.ForeignKey(Exercise, on_delete=models.CASCADE)
