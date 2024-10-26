from django.shortcuts import render, get_object_or_404, redirect
from .models import Tratamiento
from .forms import TratamientoForm

# Listado de tratamientos
def lista_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return render(request, 'tratamientos/lista_tratamientos.html', {'tratamientos': tratamientos})

# Crear un nuevo tratamiento
def crear_tratamiento(request):
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tratamientos')
    else:
        form = TratamientoForm()
    return render(request, 'tratamientos/crear_tratamiento.html', {'form': form})

# Editar un tratamiento
def editar_tratamiento(request, tratamiento_id):
    tratamiento = get_object_or_404(Tratamiento, id=tratamiento_id)
    if request.method == 'POST':
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return redirect('lista_tratamientos')
    else:
        form = TratamientoForm(instance=tratamiento)
    return render(request, 'tratamientos/editar_tratamiento.html', {'form': form, 'tratamiento': tratamiento})

# Eliminar un tratamiento
def eliminar_tratamiento(request, tratamiento_id):
    tratamiento = get_object_or_404(Tratamiento, id=tratamiento_id)
    if request.method == 'POST':
        tratamiento.delete()
        return redirect('lista_tratamientos')
    return render(request, 'tratamientos/eliminar_tratamiento.html', {'tratamiento': tratamiento})
