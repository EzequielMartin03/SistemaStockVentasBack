from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/categories') 
        else:
            messages.error(request, 'Credenciales incorrectas')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('login')

def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Usuario creado exitosamente')
    return redirect('user_list')

def edit_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verificar que el ID esté presente
        if not user_id:
            messages.error(request, 'El ID del usuario es obligatorio')
            return redirect('user_list')

        try:
            user = User.objects.get(id=user_id)

            # Verificar si los datos de username y email son correctos
            user.username = username
            user.email = email

            # Si la contraseña es proporcionada, actualizarla
            if password:
                user.set_password(password)
            
            user.save()
            messages.success(request, 'Usuario actualizado exitosamente')
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe')
        except Exception as e:
            # Capturar cualquier otro error
            messages.error(request, f'Ocurrió un error: {e}')

    return redirect('user_list')


def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST['id']
        users_count = User.objects.count()
        if users_count > 1:
            user = User.objects.get(id=user_id)
            user.delete()
            messages.success(request, 'Usuario eliminado exitosamente')
        else:
            messages.error(request, 'No se puede eliminar el único usuario restante')
    return redirect('user_list')