from django import forms

from .models import Teacher
from .models import Subject


class AppendTeacher(forms.Form):
    name = forms.CharField(max_length=50, label='Направление')
    lesson = forms.ModelChoiceField(queryset=Subject.objects.values_list('sub', flat = True))


