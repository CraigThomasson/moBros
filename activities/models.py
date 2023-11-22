from django.contrib.auth.models import User
from django.db import models
from categories.models import Categories


# Create your models here.
class Exercise(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    description = models.TextField()
    timeframe = models.IntegerField()
    difficulty = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ExerciseSteps(models.Model):
    """
    Create multiple steps for single exercise
    """
    step = models.CharField
    exercise = models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)
