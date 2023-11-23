from django import forms
from .models import Exercise


class ExerciseForm(forms.Form):
    class Meta:
        model = Exercise
        exclude = ('user',)
