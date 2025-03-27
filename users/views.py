from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import CustomUser

# Usar el CustomUser
User = get_user_model()

# Vista para login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.session['username'] = user.username
            return redirect('/categories') 
        else:
            messages.error(request, 'Credenciales incorrectas')
    return render(request, 'login.html')


# Vista para logout
def logoutView(request):
    logout(request)
    return redirect('login')


# Vista para listar los usuarios
def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def add_user(request):
    roles = CustomUser.ROLE_CHOICES  # Pasa los roles disponibles al template
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
        else:
            try:
                # Crear el usuario
                user = User.objects.create_user(username=username, email=email, password=password)

                # Asignar el rol al usuario
                user.role = role
                user.save()

                messages.success(request, 'Usuario creado exitosamente')
            except Exception as e:
                messages.error(request, f'Error al crear el usuario: {e}')
    return redirect('user_list')


# Vista para editar un usuario
def edit_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')  # Obtener el rol desde el formulario

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

            # Actualizar el rol
            user.role = role
            user.save()

            messages.success(request, 'Usuario actualizado exitosamente')
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe')
        except Exception as e:
            # Capturar cualquier otro error
            messages.error(request, f'Ocurrió un error: {e}')

    return redirect('user_list')


# Vista para eliminar un usuario
def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST['id']
        users_count = User.objects.count()
        if users_count > 1:
            try:
                user = User.objects.get(id=user_id)
                user.delete()
                messages.success(request, 'Usuario eliminado exitosamente')
            except User.DoesNotExist:
                messages.error(request, 'El usuario no existe')
        else:
            messages.error(request, 'No se puede eliminar el único usuario restante')
    return redirect('user_list')
