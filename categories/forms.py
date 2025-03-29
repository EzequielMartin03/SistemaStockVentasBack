from django import forms
from products.models import Category  # Se importa desde la app correcta

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': 'Nombre de la Categoría'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}
