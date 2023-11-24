from django.shortcuts import render, redirect
from .forms import ProfileForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'user_profiles/register.html', {'form': form})