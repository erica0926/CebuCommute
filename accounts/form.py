from django.forms import ModelForm
from django import forms
from .models import Passenger


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Passenger
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
