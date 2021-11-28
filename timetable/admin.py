from django.contrib import admin
from .models import Group, Teacher, Table, Subject, Age

admin.site.register(Age)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Table)
admin.site.register(Subject)