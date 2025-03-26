from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # O la URL que desees
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('login')


@login_required

def index(request):
    return render(request, 'index.html')

