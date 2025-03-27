from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('list', views.userList, name='userList'),
    path('new', views.userCreate, name='userCreate'),
    path('edit/<int:pk>/', views.userUpdate, name='userUpdate'),
    path('delete/<int:pk>/', views.userDelete, name='userDelete'),

]