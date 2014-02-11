from django.forms import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User
from .models import *


class DemoForm(ModelForm):
    class Meta:
        model = Ciudadela


