# Generated by Django 2.2.24 on 2021-11-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0012_auto_20211129_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=20)),
            ],
        ),
    ]
