from django import forms
from .models import Mytimetable

class EnterForm(forms.ModelForm):
    class Meta:
        model = Mytimetable
        fields = ('login', 'password',)