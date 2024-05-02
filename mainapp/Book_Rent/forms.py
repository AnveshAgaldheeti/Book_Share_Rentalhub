from django import forms
from .models import Sell_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Sell_form(forms.ModelForm):
    class Meta:
        model=Sell_model
        fields="__all__"



class signupform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
