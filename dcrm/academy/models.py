from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=150, blank=False)
    course_date_begin = models.DateTimeField(blank=False)
    course_time_begin = models.TimeField(blank=False)
    course_location = models.CharField(max_length=100)
    course_tutor = models.CharField(max_length=100)
    course_date_end = models.DateTimeField()
    course_time_end = models.TimeField()
    course_standard = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_name} {self.course_date_begin}"


class Attendee(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    first_name = models.CharField(max_length=20, blank=False)
    fathers_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
