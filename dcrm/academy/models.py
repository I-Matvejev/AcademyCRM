from django.db import models
from django.core.validators import RegexValidator

name_validator_rus = RegexValidator(r'^([А-Я][а-я-,. ]+[ ]*)+$')
name_validator_eng = RegexValidator(r'^([A-Z][-,a-z. ]+[ ]*)+$')


class Course(models.Model):

    COURSE_STATUS = [('Запланирован', 'Запланирован'), ('Подтвержден', 'Подтвержден'), ('Проведен', 'Проведен'), ('Отменен', 'Отменен')]

    course_name = models.CharField(max_length=150)
    course_date_begin = models.DateField()
    course_time_begin = models.TimeField(default='10:00')
    course_location = models.CharField(max_length=100, default='127083, г. Москва, ул. Верхняя Масловка д. 20, стр. 2')
    course_tutor = models.CharField(max_length=100)
    course_date_end = models.DateField()
    course_time_end = models.TimeField(default='17:00')
    course_status = models.CharField(choices=COURSE_STATUS, default='Запланирован', verbose_name=('Статус'))

    def __str__(self):
        return f"{self.course_name} {self.course_date_begin}"


class Attendee(models.Model):

    CONTRACT_CHOICES = [('Не направлен', 'Не направлен'), ('Направлен', 'Направлен'), ('Подписан', 'Подписан')]
    INVOICE_CHOICES = [('Не оплачен', 'Не оплачен'), ('Оплачен', 'Оплачен'), ('Постоплата', 'Постоплата')]

    attendee_course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendee_last_name_rus = models.CharField(max_length=50, validators=[name_validator_rus])
    attendee_first_name_rus = models.CharField(max_length=20, validators=[name_validator_rus])
    attendee_fathers_name_rus = models.CharField(max_length=50, validators=[name_validator_rus])
    attendee_last_name_eng = models.CharField(max_length=50, validators=[name_validator_eng])
    attendee_first_name_eng = models.CharField(max_length=20, validators=[name_validator_eng])
    attendee_email = models.EmailField(max_length=100)
    attendee_phone = models.CharField(max_length=20)
    attendee_company = models.CharField(max_length=100)
    attendee_position = models.CharField(max_length=50)
    attendee_contract_number = models.CharField(max_length=25)
    attendee_contract_status = models.CharField(choices=CONTRACT_CHOICES, default='Не направлен', verbose_name=('Статус договора'))
    attendee_invoice_status = models.CharField(choices=INVOICE_CHOICES, default='Не оплачен', verbose_name=('Статус счета'))
    attendee_course_price = models.CharField(max_length=25)
    attendee_contact_last_name_rus = models.CharField(blank=True, max_length=50, validators=[name_validator_rus])
    attendee_contact_first_name_rus = models.CharField(blank=True, max_length=20, validators=[name_validator_rus])
    attendee_contact_fathers_name_rus = models.CharField(blank=True, max_length=50, validators=[name_validator_rus])
    attendee_contact_email = models.EmailField(blank=True, max_length=100)
    attendee_contact_phone = models.CharField(blank=True, max_length=20)
    attendee_contact_position = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return f"{self.attendee_first_name_rus} {self.attendee_last_name_rus}"
