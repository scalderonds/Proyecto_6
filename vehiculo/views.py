from django.shortcuts import render, HttpResponse, redirect
from .forms import VehiculoForm

# Create your views here.


def index(request):
    return HttpResponse('<h1> Catálogo de Vehículos </h1>')


def ingresar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'ingresar_vehiculo.html', {'form': form})
