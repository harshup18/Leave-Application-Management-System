from django import forms
from .models import Application
from faculty.models import Faculty


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['docs', 'description', 'faculty', 'from_Date', 'to_Date']
