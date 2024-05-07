import datetime
import io

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count, Case, When, Q
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus.tables import Table
from reportlab.platypus import SimpleDocTemplate


from .models import Course, Attendee
from .forms import NewCourseForm, CourseAttendeesForm


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Возникла проблема, попробуйте еще раз...")
    upcoming_courses = Course.objects.filter(course_date_begin__gt=datetime.date.today()).order_by('course_date_begin')[:5].annotate(number_of_attendees=Count('attendee')).annotate(number_of_attendees_approved=Count(Case(When(Q(attendee__attendee_invoice_status='Оплачен') | Q(attendee__attendee_contract_status='Подписан') | Q(attendee__attendee_invoice_status='Постоплата'), then=1))))
    return render(request, 'home.html', {'upcoming_courses': upcoming_courses})


def logout_user(request):
    logout(request)
    return redirect('home')


def new_course(request):
    form = NewCourseForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                new_course = form.save()
                messages.success(request, "Добавлен новый курс!")
                return redirect('all_courses')
        return render(request, 'new_course.html', {'form': form})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def all_courses(request):
    if request.user.is_authenticated:
        courses = Course.objects.all().order_by('-id').annotate(number_of_attendees=Count('attendee')).annotate(number_of_attendees_invoice_paid=Count(Case(When(Q(attendee__attendee_invoice_status='Оплачен') | Q(attendee__attendee_invoice_status='Постоплата'), then=1))))
        return render(request, 'all_courses.html', {'courses': courses})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')

# def course_detail(request, pk):
#     if request.user.is_authenticated:
#         course_detail = Course.objects.get(id=pk)
#         return render(request, 'course_detail.html', {'course_detail': course_detail})
#     else:
#         messages.success(request, "Вы не авторизованы для просмотра этой страницы!")
#         return redirect('home')


def delete_course(request, pk):
    if request.user.is_authenticated:
        delete_it = Course.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Курс успешно удален!")
        return redirect('home')
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def update_course(request, pk):
    if request.user.is_authenticated:
        current_course = Course.objects.get(id=pk)
        form = NewCourseForm(request.POST or None, instance=current_course)
        if form.is_valid():
            form.save()
            messages.success(request, "Данные успешно изменены!")
            return redirect('all_courses')
        return render(request, 'update_course.html', {'form': form, 'current_course': current_course})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def course_attendees_all(request, course_id):
    if request.user.is_authenticated:
        all_attendees = Attendee.objects.filter(attendee_course_id=course_id).order_by('attendee_company')
        current_course = Course.objects.get(pk=course_id)
        part_of_course = Attendee.objects.filter(attendee_course_id=course_id).exclude(attendee_sub_course__isnull=True).exclude(attendee_sub_course__exact='')
        return render(request, 'course_attendees_all.html', {'all_attendees': all_attendees, 'course_id': course_id, 'current_course': current_course, 'part_of_course': part_of_course})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')

# def attendee_detail(request, pk):
#     if request.user.is_authenticated:
#         attendee_detail = Attendee.objects.get(id=pk)
#         return render(request, 'attendee_detail.html', {'attendee_detail': attendee_detail})
#     else:
#         messages.success(request, "Вы не авторизованы для просмотра этой страницы!")
#         return redirect('home')


def delete_attendee(request, pk):
    if request.user.is_authenticated:
        delete_it = Attendee.objects.get(id=pk)
        course_id_number = delete_it.attendee_course_id.id
        delete_it.delete()
        messages.success(request, "Слушатель успешно удален!")
        return redirect('course_attendees_all', course_id_number)
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def update_attendee(request, pk):
    if request.user.is_authenticated:
        current_attendee = Attendee.objects.get(id=pk)
        form = CourseAttendeesForm(request.POST or None, instance=current_attendee)
        if form.is_valid():
            form.save()
            messages.success(request, "Данные успешно изменены!")
            return redirect('course_attendees_all', current_attendee.attendee_course_id.id)
        return render(request, 'update_attendee.html', {'form': form, 'current_attendee': current_attendee})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def add_attendee(request, course_id):
    form = CourseAttendeesForm(request.POST or None, initial={"attendee_course_id": course_id})
    all_registered_attendees = Attendee.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                new_attendee = form.save()
                messages.success(request, "Добавлен новый слушатель!")
                return redirect('course_attendees_all', new_attendee.attendee_course_id.id)
        return render(request, 'add_attendee.html', {'form': form, 'all_registered_attendees': all_registered_attendees})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def attendees(request):
    if request.user.is_authenticated:
        attendees_list = Attendee.objects.all().order_by('attendee_last_name_rus')
        return render(request, 'attendees.html', {'attendees_list': attendees_list})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def save_to_pdf(request, course_id):
    buffer = io.BytesIO()
    pdf_object = canvas.Canvas(buffer, pagesize=A4, bottomup=0)
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'C:\\Users\\matve-il\\PycharmProjects\\dcrm\\dcrm\\academy\\djserif\\DejaVuSerif.ttf'))
    font_name = "DejaVuSerif"
    pdf_object.setFont(font_name, 12)

    text_object = pdf_object.beginText()
    text_object.setTextOrigin(20, 20)

    attendees_to_print = Attendee.objects.filter(attendee_course_id=course_id).order_by('attendee_last_name_rus')
    current_course = Course.objects.get(pk=course_id)

    lines = []

    for attendee in attendees_to_print:
        lines.append("")
        lines.append(f"Фамилия: {attendee.attendee_last_name_rus}")
        lines.append(f"Имя: {attendee.attendee_first_name_rus}")
        lines.append(f"Отчество: {attendee.attendee_fathers_name_rus}")
        lines.append(f"Компания: {attendee.attendee_company}")
        lines.append(f"Должность: {attendee.attendee_position}")
        if attendee.attendee_sub_course:
            lines.append(f"Часть курса: {attendee.attendee_sub_course}")
        lines.append("")
        lines.append("=======================")

    text_object.textLine(" ")
    text_object.textLine(f"Слушатели курса: {current_course.course_name} {current_course.course_date_begin}")
    text_object.textLine(" ")

    for line in lines:
        text_object.textLine(line)

    pdf_object.drawText(text_object)
    pdf_object.showPage()
    pdf_object.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"{current_course}.pdf")
