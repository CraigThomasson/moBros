from django.urls import path
from .views import log_completed_activity, activity_session_in_progress

urlpatterns = [
    path('log_completed_activity/', log_completed_activity, name='log_completed_activity'),
    path('session/', activity_session_in_progress, name='active_session'),
]
