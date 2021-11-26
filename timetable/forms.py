from django import forms

from .models import Teacher


class AppendTeacher(forms.Form):
    name = forms.ModelChoiceField(queryset=Teacher.objects.all().order_by('name'))
    lesson = forms.CharField(max_length=50)
