# Generated by Django 5.0.2 on 2024-03-18 11:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_alter_attendee_attendee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='attendee_city',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-Я]*$')]),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='attendee_fathers_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-Я]*$')]),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='attendee_first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-Я]*$')]),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='attendee_last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-Я]*$')]),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='attendee_phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[+][7]-[0-9]{3}-[0-9]{3}-[0-9]{4}')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-Я]*$')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_tutor',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Zа-яА-Я]*$')]),
        ),
    ]
