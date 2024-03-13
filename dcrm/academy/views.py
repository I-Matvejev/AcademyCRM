from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Course, Attendee


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
    pass


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
