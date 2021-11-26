from django import forms

from .models import Teacher


class AppendTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'lesson',)
