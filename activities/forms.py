from django import forms
from .models import Activity


class EditActivityForm(forms.Form):
    class Meta:
        model = Activity
        exclude = ('user',)
