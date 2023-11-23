from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'fitness_level', 'mindfulness_level', 'exercises']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user