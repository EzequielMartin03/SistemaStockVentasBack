from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




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

def userList(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Solo para pruebas, quita esta línea en producción
def userCreate(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if user_id:  # Editar usuario existente
            user = User.objects.get(id=user_id)
            user.username = username
            user.email = email
            user.save()
            messages.success(request, "Usuario actualizado correctamente.")
        else:  # Crear nuevo usuario
            if not password:
                messages.error(request, "La contraseña es obligatoria para nuevos usuarios.")
                return redirect('userList')

            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Usuario creado correctamente.")

        return redirect('userList')


def userUpdate(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('userList')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

def userDelete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('userList')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
