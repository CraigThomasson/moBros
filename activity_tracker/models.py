from django.db import models
from django.contrib.auth.models import User
from activities.models import Activity 

class CompletedActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date_completed = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity.name} completed by {self.user.username} on {self.date_completed}"
