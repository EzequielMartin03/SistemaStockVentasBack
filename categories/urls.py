# categories/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='category_list'),
    # Si tienes las vistas para crear, actualizar y eliminar, puedes descomentar las siguientes líneas:
    # path('categories/create/', views.category_create, name='category_create'),
    # path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    # path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
]
