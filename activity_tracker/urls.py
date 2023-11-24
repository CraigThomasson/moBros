from django.urls import path
from .views import log_completed_activity, activity_session_in_progress, \
    add_activity_to_activity_tracker, finalize_session

urlpatterns = [
    path('log_completed_activity/', log_completed_activity, name='log_completed_activity'),
    path('session/', activity_session_in_progress, name='active_session'),
    path('session/add/<int:activity_id>/', add_activity_to_activity_tracker, name='add_activity_to_session'),
    path('session/finalize/', finalize_session, name='finalize_session'),
]
