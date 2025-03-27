from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('list', views.user_list, name='user_list'), 
    path('add', views.add_user, name='add_user'),  
    path('edit', views.edit_user, name='edit_user'),  
    path('delete', views.delete_user, name='delete_user'), 
]
