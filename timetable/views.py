from django.shortcuts import render, get_object_or_404, redirect
from .forms import AppendTeacher
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
    form = AppendTeacher(request.POST)
    if form.is_valid():
        teacher = form.save(commit=False)
        teacher.save()
    return render(request, 'timetable/new_teacher.html')

