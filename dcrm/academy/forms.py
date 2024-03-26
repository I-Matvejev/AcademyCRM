from django import forms
from .models import Course, Attendee


class NewCourseForm(forms.ModelForm):
    course_name = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Название курса", "class": "form-control"}), label="")
    course_date_begin = forms.DateField(widget=forms.widgets.DateInput(format='%d.%m.%Y', attrs={"placeholder": "Дата начала", "class": "form-control"}), input_formats=['%d.%m.%Y'], label="")
    course_time_begin = forms.TimeField(initial='10:00', widget=forms.widgets.TimeInput(attrs={"placeholder": "Время начала", "class": "form-control"}), label="Время начала")
    course_location = forms.CharField(initial='127083, г. Москва, ул. Верхняя Масловка д. 20, стр. 2', widget=forms.widgets.TextInput(attrs={"placeholder": "Место проведения", "class": "form-control"}), label="Адрес")
    course_tutor = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Преподаватель", "class": "form-control"}), label="")
    course_date_end = forms.DateField(widget=forms.widgets.DateInput(format='%d.%m.%Y', attrs={"placeholder": "Дата окончания", "class": "form-control"}), input_formats=['%d.%m.%Y'], label="")
    course_time_end = forms.TimeField(initial='17:00', widget=forms.widgets.TimeInput(attrs={"placeholder": "Время окончания", "class": "form-control"}), label="Время окончания")
    course_status = forms.Select(attrs={"placeholder": "Статус", "class": "form-control"})

    class Meta:
        model = Course
        exclude = ("course",)


class CourseAttendeesForm(forms.ModelForm):
    attendee_course_id = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.widgets.HiddenInput(attrs={"placeholder": "Название курса", "class": "form-control"}), label="")
    attendee_last_name_rus = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Фамилия", "class": "form-control"}), label="")
    attendee_first_name_rus = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Имя", "class": "form-control"}), label="")
    attendee_fathers_name_rus = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Отчество", "class": "form-control"}), label="")
    attendee_last_name_eng = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Surname", "class": "form-control"}), label="")
    attendee_first_name_eng = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Name", "class": "form-control"}), label="")
    attendee_email = forms.EmailField(widget=forms.widgets.TextInput(attrs={"placeholder": "Электронная почта", "class": "form-control"}), label="")
    attendee_phone = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Телефон", "class": "form-control"}), label="")
    attendee_company = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Компания", "class": "form-control"}), label="")
    attendee_position = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder": "Должность", "class": "form-control"}), label="")
    attendee_contract_number = forms.CharField(required=False, max_length=25, widget=forms.widgets.TextInput(attrs={"placeholder": "Номер договора", "class": "form-control"}), label="")
    attendee_contract_status = forms.Select(attrs={"placeholder": "Статус договора", "class": "form-control"})
    attendee_invoice_status = forms.Select(attrs={"placeholder": "Статус счета", "class": "form-control"})
    attendee_course_price = forms.CharField(max_length=25, widget=forms.widgets.TextInput(attrs={"placeholder": "Стоимость", "class": "form-control"}), label="")
    attendee_contact_last_name_rus = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Фамилия контактного лица (опционально)", "class": "form-control"}), label="")
    attendee_contact_first_name_rus = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Имя контактного лица (опционально)", "class": "form-control"}), label="")
    attendee_contact_fathers_name_rus = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Отчество контактного лица (опционально)", "class": "form-control"}), label="")
    attendee_contact_email = forms.EmailField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Электронная почта контактного лица (опционально)", "class": "form-control"}), label="")
    attendee_contact_phone = forms.CharField(required=False,  widget=forms.widgets.TextInput(attrs={"placeholder": "Телефон контактного лица (опционально)", "class": "form-control"}), label="")
    attendee_contact_position = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder": "Должность контактного лица (опционально)", "class": "form-control"}), label="")

    class Meta:
        model = Attendee
        exclude = ("attendee",)
