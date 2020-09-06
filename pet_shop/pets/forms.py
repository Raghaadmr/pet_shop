from django import forms
from .models import Pets

class PetsForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = '__all__'
        
