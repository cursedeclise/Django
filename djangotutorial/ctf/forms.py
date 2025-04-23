from django import forms

from .models import *


class ChallengeForm(forms.ModelForm):
    class Meta:
        model=challenge
        fields= ['name', 'summary', 'flag_value', 'points']