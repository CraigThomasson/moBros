from django.db import models
from django.contrib.auth.models import User
from activities.models import Activity


class ActivitySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ManyToManyField(Activity)
    date_created = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    date_completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Session {self.user.username} on {self.date_created}"


class CompletedActivity(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    session = models.ForeignKey(ActivitySession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.session.activity.name} completed by {self.user.username} on {self.date_completed}"

