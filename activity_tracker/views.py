import datetime

from django.shortcuts import render, redirect
from .models import CompletedActivity, ActivitySession
from activities.models import Activity
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Count, DateField
from django.db.models.functions import TruncDate


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
    active_session = ActivitySession.objects.filter(user=request.user, active=True)
    f = ActivitySession.objects.get(id=active_session[0].id)
    f.active = False
    f.date_completed = datetime.date.today()
    f.save()
    return redirect('view_profile')


def log_completed_activity(request):
    user_profile = request.user.profile
    activities = user_profile.activities.all()

    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        activity = Activity.objects.get(id=activity_id)
        CompletedActivity.objects.create(user=request.user, activity=activity, date_completed=date.today())
        return redirect('log_completed_activity')

    #SESSIONs
    # completed_activities = CompletedActivity.objects.filter(user=request.user)

    # activity_data = completed_activities.annotate(date=TruncDate('date_completed')).values('date').annotate(count=Count('id')).values('date', 'count')

    # activity_dates = [activity['date'].strftime("%Y-%m-%d") for activity in activity_data]
    # activity_counts = [activity['count'] for activity in activity_data]

    return render(request, 'activity_tracker/log_completed_activity.html', {
        'activities': activities,
        # 'activity_dates': activity_dates,
        # 'activity_counts': activity_counts
    })
