# Generated by Django 5.0.2 on 2024-03-12 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=150)),
                ('course_date_begin', models.DateTimeField()),
                ('course_time_begin', models.TimeField()),
                ('course_location', models.CharField(max_length=100)),
                ('course_tutor', models.CharField(max_length=100)),
                ('course_date_end', models.DateTimeField()),
                ('course_time_end', models.TimeField()),
                ('course_standard', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=20)),
                ('fathers_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='academy.course')),
            ],
        ),
    ]
