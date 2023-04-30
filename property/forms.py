
from django import forms

from .models import PropertyBook




class PropertyBookForm(forms.ModelForm):
    class Meta:
        model = PropertyBook
        fields = ['date_from','date_to','guest','childern']