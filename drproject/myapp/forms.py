from django import forms
from .models import *

class appoinmentform(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'