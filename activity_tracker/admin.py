from django.contrib import admin
from .models import CompletedActivity, ActivitySession

admin.site.register(CompletedActivity)
admin.site.register(ActivitySession)
