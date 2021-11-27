from django.shortcuts import render, get_object_or_404, redirect
from .forms import *

def index(request):
    return render(request, 'timetable/index.html')

def data_for_user(request):
    return render(request, 'timetable/data_for_user.html')

def lessons_for_user(request):
    return render(request, 'timetable/lessons_for_user.html')

def enter(request):
    return render(request, 'registration/login.html')

def index_for_admin(request):
    return render(request, 'timetable/index_for_admin.html')

def new_teacher(request):
    if request.method == "POST":
        form = AppendTeacher(request.POST)
        if form.is_valid():
            teacher = Teacher()
            teacher.name = form.cleaned_data.get("name")
            teacher.lesson = form.cleaned_data.get("lesson")
            teacher.save()
    else:
        form = AppendTeacher()
    return render(request, 'timetable/new_teacher.html',{
          'form': form,})