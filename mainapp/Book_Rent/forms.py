from django import forms
from .models import Sell_model
class Sell_form(forms.ModelForm):
    class Meta:
        model=Sell_model
        fields="__all__"
