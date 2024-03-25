# Generated by Django 5.0.2 on 2024-03-25 07:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0007_alter_attendee_attendee_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='attendee_gender',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F')], default='Male'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='attendee_city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='attendee_fathers_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^([A-ZА-Я][а-я-,a-z. ]+[ ]*)+$')]),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='attendee_first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^([A-ZА-Я][а-я-,a-z. ]+[ ]*)+$')]),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='attendee_last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^([A-ZА-Я][а-я-,a-z. ]+[ ]*)+$')]),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='attendee_phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_tutor',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^([A-ZА-Я][а-я-,a-z. ]+[ ]*)+$')]),
        ),
    ]
