from django.contrib import admin
from .models import Group, Teacher, Table, Subject, Age, Days_of_the_week, Time, Cabinets

admin.site.register(Age)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Table)
admin.site.register(Subject)
admin.site.register(Cabinets)
admin.site.register(Time)
admin.site.register(Days_of_the_week)