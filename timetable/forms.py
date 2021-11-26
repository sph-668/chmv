from django import forms

from .models import Teacher

class AppendTeacher(forms.Form):
    teachers = forms.ChoiceField(widget=forms.Select, choices=[])
    class Meta:
        fields = ('name', 'lesson',)

    def __init__(self, *args, **kwargs):
        super(AppendTeacher, self).__init__(*args, **kwargs)
        self.fields['name'].choices = [x.name for x in Teacher.objects.all()]

