from django.db import models
from django.core.validators import RegexValidator

name_validator_rus = RegexValidator(r'^([А-Я][а-я-,. ]+[ ]*)+$')
name_validator_eng = RegexValidator(r'^([A-Z][-,a-z. ]+[ ]*)+$')


class Course(models.Model):

    COURSE_STATUS = [('Запланирован', 'Запланирован'), ('Подтвержден', 'Подтвержден'), ('Проведен', 'Проведен'), ('Отменен', 'Отменен')]

    course_name = models.CharField(max_length=150, blank=False)
    course_date_begin = models.DateField(blank=False)
    course_time_begin = models.TimeField(blank=False)
    course_location = models.CharField(max_length=100)
    course_tutor = models.CharField(max_length=100)
    course_date_end = models.DateField()
    course_time_end = models.TimeField()
    course_standard = models.CharField(max_length=100)
    course_status = models.CharField(blank=False, choices=COURSE_STATUS, default='planned', verbose_name=('Статус'))

    def __str__(self):
        return f"{self.course_name} {self.course_date_begin}"


class Attendee(models.Model):

    GENDER_CHOICES = [('M', 'M'), ('F', 'F')]

    attendee_course_id = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False)
    attendee_last_name_rus = models.CharField(max_length=50, blank=False, validators=[name_validator_rus], default='')
    attendee_first_name_rus = models.CharField(max_length=20, blank=False, validators=[name_validator_rus], default='')
    attendee_fathers_name_rus = models.CharField(max_length=50, validators=[name_validator_rus], default='')
    attendee_last_name_eng = models.CharField(max_length=50, blank=False, validators=[name_validator_eng], default='')
    attendee_first_name_eng = models.CharField(max_length=20, blank=False, validators=[name_validator_eng], default='')
    attendee_fathers_name_eng = models.CharField(max_length=50, validators=[name_validator_eng], default='')
    attendee_gender = models.CharField(blank=False, choices=GENDER_CHOICES, default='M', verbose_name=('Пол'))
    attendee_email = models.EmailField(max_length=100, blank=False)
    attendee_phone = models.CharField(max_length=20, blank=False)
    attendee_company = models.CharField(max_length=100)
    attendee_position = models.CharField(max_length=50, default='')
    attendee_city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.attendee_first_name_rus} {self.attendee_last_name_rus}"
