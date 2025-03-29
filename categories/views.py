from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Category
from .forms import CategoryForm

def category_list(request):
    """Muestra todas las categorías disponibles."""
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
def category_create(request):
    """Permite crear una nueva categoría."""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creada exitosamente.")
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, pk):
    """Permite modificar una categoría existente."""
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría actualizada exitosamente.")
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    """Elimina una categoría si no tiene productos asociados."""
    category = get_object_or_404(Category, pk=pk)
    
    # Verifica si hay productos en la categoría antes de eliminarla
    if category.product_set.exists():
        messages.error(request, "No se puede eliminar la categoría, tiene productos asignados.")
    else:
        category.delete()
        messages.success(request, "Categoría eliminada exitosamente.")
    
    return redirect('category_list')
