from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
from rest_framework_simplejwt.tokens import RefreshToken


from django.contrib.auth.models import User

def get_users(request):
    # Obtener todos los usuarios y sus datos relevantes (username y role)
    users = User.objects.all().values('id', 'username', 'is_staff')  # 'is_staff' es un campo que puede ser usado para roles
    return JsonResponse({'users': list(users)})
def index(request):
    return HttpResponse("¡Vista de prueba exitosa!")
@csrf_exempt
def Login(request):
    if request.method == "POST":
        try:
            # Recibir datos en formato JSON
            data = json.loads(request.body)

            username = data.get("username")
            password = data.get("password")

            # Validar que el usuario y la contraseña estén presentes
            if not username or not password:
                return JsonResponse({"detail": "Username and password are required."}, status=400)

            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Generar el token JWT usando `RefreshToken`
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                # Responder con el token JWT y un mensaje de éxito
                return JsonResponse({
                    "detail": "Login successful.",
                    "access_token": access_token  # Incluir el token JWT en la respuesta
                }, status=200)

            else:
                # Responder con un error si las credenciales son incorrectas
                return JsonResponse({"detail": "Invalid credentials."}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"detail": "Invalid JSON format."}, status=400)

    else:
        # Si el método no es POST, responder con un error 405
        return JsonResponse({"detail": "Method not allowed."}, status=405)

def Logout(request):
    logout(request)
    return redirect("/login")
