from django.shortcuts import render, redirect, reverse, get_object_or_404

from activities.forms import EditActivityForm
from activities.models import Activity
from categories.models import Categories
from user_profile.models import Profile


# Create your views here.
def activity_list(request):
    categories = list(Categories.objects.all())
    activity_list = list(Activity.objects.all())

    ctx = {
        'categories': categories,
        'activity_list': activity_list,
    }

    return render(request, 'activities/activities.html', ctx)


def edit_activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    form = EditActivityForm(instance=activity)
    if request.method == 'POST':
        form = EditActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect(reverse('activities'))
    ctx = {
        'activity': activity,
        'form': form
    }
    return render(request, 'activities/edit_activity.html', ctx)
