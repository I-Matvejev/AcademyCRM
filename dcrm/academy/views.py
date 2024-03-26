import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count

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
    upcoming_courses = Course.objects.filter(course_date_begin__gte=datetime.date.today()).order_by('course_date_begin')[:5].annotate(number_of_attendees=Count('attendee'))
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
    courses = Course.objects.all().order_by('-id')
    return render(request, 'all_courses.html', {'courses': courses})


def course_detail(request, pk):
    if request.user.is_authenticated:
        course_detail = Course.objects.get(id=pk)
        return render(request, 'course_detail.html', {'course_detail': course_detail})
    else:
        messages.success(request, "Вы не авторизованы для просмотра этой страницы!")
        return redirect('home')


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
        return render(request, 'update_course.html', {'form': form})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def course_attendees_all(request, course_id):
    all_attendees = Attendee.objects.filter(attendee_course_id=course_id).order_by('attendee_last_name_rus')
    current_course = Course.objects.get(pk=course_id)
    return render(request, 'course_attendees_all.html', {'all_attendees': all_attendees, 'course_id': course_id, 'current_course': current_course})


def attendee_detail(request, pk):
    if request.user.is_authenticated:
        attendee_detail = Attendee.objects.get(id=pk)
        return render(request, 'attendee_detail.html', {'attendee_detail': attendee_detail})
    else:
        messages.success(request, "Вы не авторизованы для просмотра этой страницы!")
        return redirect('home')


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
            return redirect('attendee_detail', current_attendee.id)
        return render(request, 'update_attendee.html', {'form': form})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def add_attendee(request, course_id):
    form = CourseAttendeesForm(request.POST or None, initial={"attendee_course_id": course_id})
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                new_attendee = form.save()
                messages.success(request, "Добавлен новый слушатель!")
                return redirect('course_attendees_all', new_attendee.attendee_course_id.id)
        return render(request, 'add_attendee.html', {'form': form})
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')


def attendees(request):
    attendees_list = Attendee.objects.all().order_by('attendee_last_name_rus')
    return render(request, 'attendees.html', {'attendees_list': attendees_list})
