from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно авторизовались!")
            return redirect('home')
        else:
            messages.success(request, "Возникла проблема, попробуйте еще раз...")
    return render(request, 'home.html', {})


def logout_user(request):
    pass
