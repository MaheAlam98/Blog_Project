from django import forms 
from .models import Categories

class category(forms.ModelForm):
    class Meta:
        model=Categories
        fields='__all__'