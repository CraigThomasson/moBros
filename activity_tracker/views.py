from django.shortcuts import render, redirect
from .models import CompletedActivity
from activities.models import Activity
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Count, DateField
from django.db.models.functions import TruncDate


def log_completed_activity(request):
    user_profile = request.user.profile
    activities = user_profile.activities.all()

    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        activity = Activity.objects.get(id=activity_id)
        CompletedActivity.objects.create(user=request.user, activity=activity, date_completed=date.today())
        return redirect('log_completed_activity')

    completed_activities = CompletedActivity.objects.filter(user=request.user)
    activity_data = completed_activities.annotate(date=TruncDate('date_completed')).values('date').annotate(count=Count('id')).values('date', 'count')

    activity_dates = [activity['date'].strftime("%Y-%m-%d") for activity in activity_data]
    activity_counts = [activity['count'] for activity in activity_data]

    return render(request, 'activity_tracker/log_completed_activity.html', {
        'activities': activities,
        'activity_dates': activity_dates,
        'activity_counts': activity_counts
    })
