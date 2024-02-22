from django import forms
from .models import *


class signupForm(forms.ModelForm):
    class Meta:
        model=addsignup
        fields='__all__'