from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from decorators import role_required

from .models import CustomUser


User = get_user_model()


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



def logoutView(request):
    logout(request)
    return redirect('login')


@role_required('Admin')
def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

@role_required('Admin')
def add_user(request):
    roles = CustomUser.ROLE_CHOICES
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
        else:
            try:
                
                user = User.objects.create_user(username=username, email=email, password=password)

               
                user.role = role
                user.save()

                messages.success(request, 'Usuario creado exitosamente')
            except Exception as e:
                messages.error(request, f'Error al crear el usuario: {e}')
    return redirect('user_list')

@role_required('Admin')
def edit_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')  

    
        if not user_id:
            messages.error(request, 'El ID del usuario es obligatorio')
            return redirect('user_list')

        try:
            user = User.objects.get(id=user_id)

           
            user.username = username
            user.email = email

            
            if password:
                user.set_password(password)

           
            user.role = role
            user.save()

            messages.success(request, 'Usuario actualizado exitosamente')
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe')
        except Exception as e:
           
            messages.error(request, f'Ocurrió un error: {e}')

    return redirect('user_list')


@role_required('Admin')
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
