from django.contrib.auth.models import User
from django.db import models
from categories.models import Categories


# Create your models here.
class Activity(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    description = models.TextField()
    timeframe = models.IntegerField()
    difficulty = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ActivitiesSteps(models.Model):
    """
    Create multiple steps for single exercise
    """
    step = models.CharField
    activity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.step