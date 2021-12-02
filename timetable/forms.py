from django import forms
from django.forms import ModelChoiceField


from .models import *

from django.forms import Field
from django.utils.translation import ugettext_lazy
Field.default_error_messages = {
    'required': ugettext_lazy("This field is mandatory."),
}

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name


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
    t = list(Time.objects.values_list('time', flat = True))
    all_times = []
    for i in range(len(t)):
        all_times.append([t[i], t[i]])
    time = forms.ChoiceField(choices=all_times)

    week = list(Days_of_the_week.objects.values_list('day', flat = True))
    days_of_the_week = []
    for i in range (len(week)):
        days_of_the_week.append([week[i], week[i]])
    day_of_week = forms.ChoiceField(choices=days_of_the_week)
    cabs = list(Cabinets.objects.values_list('cab', flat = True))
    all_cabinets = []
    for i in range (len(cabs)):
        all_cabinets.append([cabs[i], cabs[i]])
    cabinet = forms.ChoiceField(choices=all_cabinets)
    group = MyModelChoiceField(queryset=Group.objects.all(), to_field_name="name", empty_label=None)

    temp = list(Teacher.objects.values_list('name', flat=True))
    all_teachers = []
    for i in range(len(temp)):
        all_teachers.append([temp[i], temp[i]])
    teacher = forms.ChoiceField(choices=all_teachers)


    subjects = list(Subject.objects.values_list('sub', flat=True))
    sub = []
    for i in range(len(subjects)):
        sub.append([subjects[i], subjects[i]])
    lesson = forms.ChoiceField(choices=sub)





class Show_on_date_user(forms.Form):
    group = MyModelChoiceField(queryset=Group.objects.all(), to_field_name="name", empty_label=None)
    date = forms.DateField()



