from django import forms
from .models import Course, Attendee


class NewCourseForm(forms.ModelForm):
    course_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Название курса", "class": "form-control"}), label="")
    course_date_begin = forms.DateField(required=True, widget=forms.widgets.DateInput(format='%d.%m.%Y', attrs={"placeholder": "Дата начала", "class": "form-control"}), input_formats=['%d.%m.%Y'], label="")
    course_time_begin = forms.TimeField(required=True, widget=forms.widgets.TimeInput(attrs={"placeholder": "Время начала", "class": "form-control"}), label="")
    course_location = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Место проведения", "class": "form-control"}), label="")
    course_tutor = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Преподаватель", "class": "form-control"}), label="")
    course_date_end = forms.DateField(widget=forms.widgets.DateInput(format='%d.%m.%Y', attrs={"placeholder": "Дата окончания", "class": "form-control"}), input_formats=['%d.%m.%Y'], label="")
    course_time_end = forms.TimeField(widget=forms.widgets.TimeInput(attrs={"placeholder": "Время окончания", "class": "form-control"}), label="")
    course_standard = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Стандарт", "class": "form-control"}), label="")

    class Meta:
        model = Course
        exclude = ("course",)


class CourseAttendeesForm(forms.ModelForm):
    attendee_course_id = forms.ModelChoiceField(queryset=Course.objects.all(), required=True, widget=forms.widgets.HiddenInput(attrs={"placeholder": "Название курса", "class": "form-control"}), label="")
    attendee_last_name_rus = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Фамилия", "class": "form-control"}), label="")
    attendee_first_name_rus = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Имя", "class": "form-control"}), label="")
    attendee_fathers_name_rus = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Отчество", "class": "form-control"}), label="")
    attendee_last_name_eng = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Surname", "class": "form-control"}), label="")
    attendee_first_name_eng = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Name", "class": "form-control"}), label="")
    attendee_fathers_name_eng = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Fathers name", "class": "form-control"}), label="")
    attendee_gender = forms.Select(attrs={"placeholder": "Пол", "class": "form-control"})
    attendee_email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Электронная почта", "class": "form-control"}), label="")
    attendee_phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Телефон: +7-999-123-4567", "class": "form-control"}), label="")
    attendee_company = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Компания", "class": "form-control"}), label="")
    attendee_position = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Должность", "class": "form-control"}), label="")
    attendee_city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Город", "class": "form-control"}), label="")

    class Meta:
        model = Attendee
        exclude = ("attendee",)


class CourseAttendeesForm2(forms.ModelForm):
    attendee_course_id = forms.ModelChoiceField(queryset=Course.objects.all(), required=True, widget=forms.widgets.HiddenInput(attrs={"placeholder": "Название курса", "class": "form-control"}), label="")
    attendee_last_name_rus = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Фамилия", "class": "form-control"}), label="")
    attendee_first_name_rus = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Имя", "class": "form-control"}), label="")
    attendee_fathers_name_rus = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Отчество", "class": "form-control"}), label="")
    attendee_last_name_eng = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Surname", "class": "form-control"}), label="")
    attendee_first_name_eng = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Name", "class": "form-control"}), label="")
    attendee_fathers_name_eng = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Fathers name", "class": "form-control"}), label="")
    attendee_gender = forms.Select(attrs={"placeholder": "Пол", "class": "form-control"})
    attendee_email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Электронная почта", "class": "form-control"}), label="")
    attendee_phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Телефон: +7-999-123-4567", "class": "form-control"}), label="")
    attendee_company = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Компания", "class": "form-control"}), label="")
    attendee_position = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Должность", "class": "form-control"}), label="")
    attendee_city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Город", "class": "form-control"}), label="")

    class Meta:
        model = Attendee
        exclude = ("attendee",)
