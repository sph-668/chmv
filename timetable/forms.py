from django import forms

from .models import Teacher
from .models import Subject
from .models import Age


class AppendTeacher(forms.Form):
    name = forms.CharField(max_length=50, label='Направление')
    subjects = list(Subject.objects.values_list('sub', flat = True))
    sub = []
    for i in range (len(subjects)):
        sub.append([subjects[i], subjects[i]])
    lesson = forms.ChoiceField(choices=sub)

class AppendGroup(forms.Form):
    name = forms.CharField(max_length=50)
    temp = list(Age.objects.values_list('age', flat = True))
    ages = []
    for i in range (len(temp)):
        ages.append([temp[i], temp[i]])
    age = forms.ChoiceField(choices=ages)



