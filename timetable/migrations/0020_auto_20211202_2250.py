# Generated by Django 2.2.24 on 2021-12-02 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0019_auto_20211130_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='week',
            new_name='day_of_week',
        ),
    ]
