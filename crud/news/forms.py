from django import forms
from .models import DailyNews

class NewsForm(forms.ModelForm):
    class Meta:
        model = DailyNews
        fields = ['newsTitle', 'details']