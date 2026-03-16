from django import forms
from .models import Details

class DetailView(forms.ModelForm):
    class Meta:
        model=Details
        fields='__all__'