from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect



def login(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/categories') 
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')



def logoutView(request):
    logout(request)
    return redirect('login')