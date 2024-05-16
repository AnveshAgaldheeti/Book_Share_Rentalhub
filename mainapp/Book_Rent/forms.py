from typing import Any
from django import forms
from .models import Sell_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class Sell_form(forms.ModelForm):
    class Meta:
        model=Sell_model
        fields=['title','author','description','categories','price','image']
    def clean_price(self):
        price=self.cleaned_data['price']
        if price<0:
            return ValidationError("price will be positive")
        else:
            return self.price


class signupform(UserCreationForm):
    email=forms.EmailField()
    def __init__(self, *args, **kwargs):
        super(signupform, self).__init__(*args, **kwargs)

        # Set placeholders for form fields
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    class Meta:
        model=User
        fields=['username','email','password1','password2']
