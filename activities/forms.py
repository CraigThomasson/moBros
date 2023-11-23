from django import forms
from .models import Activity


class EditActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ('user',)
        fields = '__all__'

