from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from .mymodule import *


def index(request):
    return render(request, 'timetable/index.html')

def data_for_user(request):
    state = 0
    message = ''
    params = []
    if request.method == "GET":
        form = Show_on_date_user(request.GET)
        if form.is_valid():
            group_ = form.cleaned_data.get("group")
            date_ = form.cleaned_data.get("date")
            day_ = parse(str(date_))
            if Table.objects.filter(group=group_, day_of_week=day_).exists():
                message = 'Расписание для группы {} на {}'.format(group_.name, day_)
                state = 1
                for i in Table.objects.filter(group=group_, day_of_week=day_):
                    params.append(i)
            else:
                message ='Занятий не найдено'
                state = -1
    else:
        form = Show_on_date_user()
        message = ''
    return render(request, 'timetable/data_for_user.html', {'form': form, 'params': params,
                                                            'message': message, 'state': state})

def lessons_for_user(request):
    return render(request, 'timetable/lessons_for_user.html')

def enter(request):
    return render(request, 'registration/login.html')

def index_for_admin(request):
    return render(request, 'timetable/index_for_admin.html')

def new_teacher(request):
    message = ''
    if request.method == "POST":
        form = AppendTeacher(request.POST)
        if form.is_valid():
            name_ = form.cleaned_data.get("name")
            lesson_ = form.cleaned_data.get("lesson")
            s = name_.replace(' ', '')
            if (not s.isalpha()):
                message = 'Некорректные данные'
            elif Teacher.objects.filter(name=name_, lesson=lesson_).exists():
                message = 'Эти данные уже были добавлены ранее'
            else:
                message = 'Добавлено'
                teacher = Teacher(name = name_, lesson = lesson_)
                teacher.save()
        else:
            message = 'Некорректные данные'
    else:
        form = AppendTeacher()
    return render(request, 'timetable/new_teacher.html',{
          'form': form, 'message': message})

def new_group(request):
    message = ''
    if request.method == "POST":
        form = AppendGroup(request.POST)
        if form.is_valid():
            name_ = form.cleaned_data.get("name")
            age_ = form.cleaned_data.get("age")
            print()
            if (not name_.isalpha()):
                message = 'Некорректные данные'
            elif Group.objects.filter(name=name_).exists():
                message = 'Такая группа уже существует'
            else:
                message = 'Добавлено'
                group = Group(name = name_, age = age_)
                group.save()
        else:
            message = 'Некорректные данные'
    else:
        form = AppendGroup()
    return render(request, 'timetable/new_group.html', {
        'form': form, 'message': message})

def new_lesson(request):
    message = ''
    if request.method == "POST":
        form = AppendLesson(request.POST)
        if form.is_valid():
            time_ = form.cleaned_data.get("time")
            day_of_week_ = form.cleaned_data.get("day_of_week")
            cabinet_ = form.cleaned_data.get("cabinet")
            group_ = form.cleaned_data.get("group")
            teacher_ = form.cleaned_data.get("teacher")
            lesson_ = form.cleaned_data.get("lesson")
            message = 'Добавлено'
            timetable = Table(time = time_, day_of_week = day_of_week_, cabinet = cabinet_, group = group_, teacher = teacher_,
                              lesson = lesson_)
            timetable.save()
        else:
            message = 'Некорректные данные'
    else:
        form = AppendLesson()
    return render(request, 'timetable/new_lesson.html', {'form': form, 'message': message})

