from django.shortcuts import render


# Create your views here.
def activity_list(request):
    categories = ''
    activity_list = ''

    ctx = {
        categories: categories,
        activity_list: activity_list,
    }

    return render(request, 'activities/activities.html', ctx)

