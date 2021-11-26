from django.contrib import admin
from .models import Group, Teacher, Table, Subject

admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Table)
admin.site.register(Subject)