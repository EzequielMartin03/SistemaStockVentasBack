from django.urls import path
from . import views
from .views import Login, Logout,index

urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('prueba/', views.index, name='index'),
    path('get_users/', views.get_users, name='get_users'),

]
