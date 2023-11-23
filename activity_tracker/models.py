from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_date = models.DateField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in minutes
    # Additional fields as required

    def __str__(self):
        return f"{self.activity_type} on {self.activity_date} by {self.user.username}"
