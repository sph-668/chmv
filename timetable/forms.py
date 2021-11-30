from django import forms

from .models import *

from django.forms import Field
from django.utils.translation import ugettext_lazy
Field.default_error_messages = {
    'required': ugettext_lazy("This field is mandatory."),
}


my_default_errors = {
    'required': 'Заполните поле',
    'invalid': 'Enter a valid value'
}




class AppendTeacher(forms.Form):
    name = forms.CharField(max_length=50, error_messages=my_default_errors, required=True)
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

class AppendLesson(forms.Form):
    time = forms.TimeField()
    week = list(Days_of_the_week.objects.values_list('day', flat = True))
    days_of_the_week = []
    for i in range (len(week)):
        days_of_the_week.append([week[i], week[i]])


class Show_on_date_user(forms.Form):
    temp = list(Group.objects.values_list('name', flat=True))
    groups = []
    for i in range(len(temp)):
        groups.append([temp[i], temp[i]])
    name = forms.ChoiceField(choices=groups)
    date = forms.DateField()



