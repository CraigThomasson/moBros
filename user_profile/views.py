from django.shortcuts import render, redirect
from .forms import ProfileForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


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


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('view_profile')  # Redirect to the profile page
    else:
        form = UserRegisterForm()
    return render(request, 'user_profiles/register.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('view_profile')  # Redirect to the profile page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'user_profiles/sign_in.html')


def log_out(request):
    logout(request)
    return redirect('home')