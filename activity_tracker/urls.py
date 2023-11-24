from django.urls import path
from .views import log_completed_activity

urlpatterns = [
    path('log_completed_activity/', log_completed_activity, name='log_completed_activity'),
]
