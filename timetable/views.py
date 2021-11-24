from django.shortcuts import render
from .models import Mytimetable

def post_list(request):
    posts = Mytimetable.objects.order_by('group')
    return render(request, 'timetable/index.html', {'posts': posts})