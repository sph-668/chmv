from django.db import models
from django.forms import Field
from django.conf import settings
from django.utils import timezone


class Group(models.Model):
    name = models.TextField()
    age = models.TextField()


class Subject(models.Model):
    sub = models.TextField()

    def __str__(self):
        return self.sub


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    lesson = models.CharField(max_length=40)


class Table(models.Model):
    time = models.TimeField()
    date = models.DateField()
    cabinet = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

# Create your models here.
