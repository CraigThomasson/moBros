from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request, 'user_profiles/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'user_profiles/edit_profile.html', {'form': form})