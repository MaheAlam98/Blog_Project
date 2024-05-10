from django import forms
from .models import Author 
class authorform(forms.ModelForm):
    class Meta:
        model=Author
        fields="__all__"