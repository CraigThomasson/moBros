import datetime

from django.shortcuts import render, redirect
from .models import CompletedActivity, ActivitySession
from activities.models import Activity
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Count, DateField
from django.db.models.functions import TruncDate
from django.core.serializers import serialize
import json


def activity_session_in_progress(request):
    active_session = ActivitySession.objects.filter(user=request.user, active=True)
#     user sends get request to add into the In Progress card
# user can add upto 5-10 activities in one session
    return render(request,
                  'activity_tracker/activity_session.html',
                  {'active_session': active_session})


def add_activity_to_activity_tracker(request, activity_id):
    active_session = ActivitySession.objects.filter(user=request.user, active=True)

    if not active_session:
        k = ActivitySession.objects.create(user_id=request.user.id)
        k.activity.add(activity_id)
        return redirect('activities')

    active_session[0].activity.add(activity_id)
    return redirect('activities')


def finalize_session(request):
    active_session = ActivitySession.objects.filter(user=request.user, active=True).first()

    if active_session:
        # Set the session as inactive and save the completion date
        active_session.active = False
        active_session.date_completed = datetime.date.today()
        active_session.save()

        # For each activity in the session, create a CompletedActivity
        for activity in active_session.activity.all():
            CompletedActivity.objects.create(
                user=request.user,
                activity=activity,
                session=active_session  # Use the specific session instance
            )

    return redirect('view_profile')


@login_required
def log_completed_activity(request):
    # Fetch completed activities
    completed_activities = CompletedActivity.objects.filter(user=request.user)

    # Count total completed activities
    total_completed_activities = completed_activities.count()

    # Count total completed sessions
    total_sessions = ActivitySession.objects.filter(
        user=request.user, 
        date_completed__isnull=False
    ).count()

    # Aggregate activities by difficulty through sessions
    activities_by_difficulty = Activity.objects.filter(
        activitysession__completedactivity__user=request.user,
        activitysession__date_completed__isnull=False
    ).values('difficulty').annotate(total=Count('id'))

    # Manually convert the QuerySet of dictionaries to JSON
    activities_by_difficulty_json = json.dumps(list(activities_by_difficulty))

    context = {
        'total_completed_activities': total_completed_activities,
        'total_sessions': total_sessions,
        'activities_by_difficulty': activities_by_difficulty_json,
    }

    return render(request, 'activity_tracker/log_completed_activity.html', context)