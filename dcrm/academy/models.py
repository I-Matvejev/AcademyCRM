from django.db import models
from django.core.validators import RegexValidator

letters_only = RegexValidator(r'^[A-ZА-Я][a-zа-я]+$')
letters_and_dash = RegexValidator(r'^[A-ZА-Я][a-zа-я]+((-[A-ZА-Я][a-zа-я]+)?)')



class Course(models.Model):
    course_name = models.CharField(max_length=150, blank=False)
    course_date_begin = models.DateField(blank=False)
    course_time_begin = models.TimeField(blank=False)
    course_location = models.CharField(max_length=100)
    course_tutor = models.CharField(max_length=100, validators=[letters_and_dash])
    course_date_end = models.DateField()
    course_time_end = models.TimeField()
    course_standard = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_name} {self.course_date_begin}"


class Attendee(models.Model):
    attendee_course_id = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False)
    attendee_last_name = models.CharField(max_length=50, blank=False, validators=[letters_and_dash])
    attendee_first_name = models.CharField(max_length=20, blank=False, validators=[letters_only])
    attendee_fathers_name = models.CharField(max_length=50, validators=[letters_only])
    attendee_email = models.EmailField(max_length=100, blank=False)
    attendee_phone = models.CharField(max_length=20, blank=False)
    attendee_company = models.CharField(max_length=100)
    attendee_city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.attendee_first_name} {self.attendee_last_name}"
