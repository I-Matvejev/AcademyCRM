from django import forms
from .models import Course, Attendee


class NewCourseForm(forms.ModelForm):
    course_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Название курса", "class": "form-control"}), label="")
    course_date_begin = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={"placeholder": "Дата начала", "class": "form-control"}), label="")
    course_time_begin = forms.TimeField(required=True, widget=forms.widgets.TimeInput(attrs={"placeholder": "Время начала", "class": "form-control"}), label="")
    course_location = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Место проведения", "class": "form-control"}), label="")
    course_tutor = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Преподаватель", "class": "form-control"}), label="")
    course_date_end = forms.DateField(widget=forms.widgets.DateInput(attrs={"placeholder": "Дата окончания", "class": "form-control"}), label="")
    course_time_end = forms.TimeField(widget=forms.widgets.TimeInput(attrs={"placeholder": "Время окончания", "class": "form-control"}), label="")
    course_standard = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Стандарт", "class": "form-control"}), label="")

    class Meta:
        model = Course
        exclude = ("course",)
