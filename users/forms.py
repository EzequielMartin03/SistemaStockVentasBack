from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser, Role



class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

