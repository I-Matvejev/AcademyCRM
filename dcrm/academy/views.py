from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Course, Attendee
from .forms import NewCourseForm


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Вы успешно авторизовались!")
            return redirect('home')
        else:
            messages.success(request, "Возникла проблема, попробуйте еще раз...")
    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    # messages.success(request, "Вы успешно вышли.")
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
    courses = Course.objects.all()
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
    all_attendees = Attendee.objects.filter(attendee_course_id=course_id)
    return render(request, 'course_attendees_all.html', {'all_attendees': all_attendees})


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
        delete_it.delete()
        messages.success(request, "Слушатель успешно удален!")
        return redirect('all_courses')
    else:
        messages.success(request, "Вы не авторизованы для этого действия!")
        return redirect('home')
