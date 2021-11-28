from django.db import models
from django.forms import Field
from django.conf import settings
from django.utils import timezone


class Group(models.Model):
    name = models.CharField(max_length=40)
    age = models.CharField(max_length=40)


class Subject(models.Model):
    sub = models.TextField()

    def __str__(self):
        return self.sub

class Age(models.Model):
    age = models.CharField(max_length=20)

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    lesson = models.CharField(max_length=40)


class Table(models.Model):
    time = models.TimeField()
    date = models.DateField()
    cabinet = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.CharField(max_length=40)
    lesson = models.CharField(max_length=40)

# Create your models here.
