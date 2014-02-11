from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from datetime import datetime
from models import *  


class LoginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Usuario o email', 'type':'text', 'autofocus':'True'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'placeholder':'Password','type':'password',}), required=True)

class DemoForm(forms.ModelForm):
    class Meta:
        model = Ciudadela


