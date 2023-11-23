from django.shortcuts import render, redirect
from .models import CompletedActivity
from activities.models import Activity
from django.contrib.auth.decorators import login_required
from datetime import date


def log_completed_activity(request):
    user_profile = request.user.profile
    activities = user_profile.activities.all()

    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        activity = Activity.objects.get(id=activity_id)
        CompletedActivity.objects.create(user=request.user, activity=activity, date_completed=date.today())
        return redirect('log_completed_activity')

    return render(request, 'activity_tracker/log_completed_activity.html', {'activities': activities})
