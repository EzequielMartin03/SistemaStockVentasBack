from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('categories/', views.category, name='category_list'),
    # path('categories/create/', views.category_create, name='category_create'),
    # path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    # path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
]
