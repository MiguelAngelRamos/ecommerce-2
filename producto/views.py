from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    productos = Producto.objects.all()
    print(productos)
    return render(
        request,
        'index.html',
        { 'productos': productos }
    )
    
def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST) # Aqui en el request.POST viene nombre, stock, categoria, imagen
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()
    return render(
        request,
        'producto_form.html',
        {'form': form }
    )        