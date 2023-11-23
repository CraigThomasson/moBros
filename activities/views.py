from django.shortcuts import render, redirect, reverse


from activities.forms import ExerciseForm
from activities.models import Exercise
from user_profile.models import Profile


# Create your views here.
def activity_list(request):
    categories = ''

    activity_list = Exercise.objects.all()

    ctx = {
        categories: categories,
        'activity_list': activity_list,
    }

    return render(request, 'activities/activities.html', ctx)


def activities_dashboard(request):
    activities = Exercise.objects.all()

    ctx = {
        'activities': activities,
    }

    return render(request, 'activities/activities_dashboard.html', ctx)


def add_new_activity(request):
    form = ExerciseForm()
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.user = Profile.objects.get(user=request.user)
            user.save()

    return redirect(reverse('activities_dashboard'))
