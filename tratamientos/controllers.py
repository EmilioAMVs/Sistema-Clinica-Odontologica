from django.shortcuts import render, get_object_or_404, redirect
from .models import Tratamiento
from .forms import TratamientoForm, TratamientoFilterForm
from hcl.models import HistoriaClinica

# Listado de tratamientos
def lista_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return render(request, 'listar_tratamientos.html', {'tratamientos': tratamientos})

# Crear un nuevo tratamiento
def crear_tratamiento(request):
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tratamientos')
    else:
        form = TratamientoForm()
    return render(request, 'crear_tratamiento.html', {'form': form})

# Editar un tratamiento
def editar_tratamiento(request, tratamiento_id):
    tratamiento = get_object_or_404(Tratamiento, id=tratamiento_id)
    if request.method == 'POST':
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return redirect('listar_tratamientos')
    else:
        form = TratamientoForm(instance=tratamiento)
    return render(request, 'editar_tratamiento.html', {'form': form, 'tratamiento': tratamiento})

def editar_tratamiento(request, tratamiento_id):
    tratamiento = get_object_or_404(Tratamiento, id=tratamiento_id)
    if request.method == 'POST':
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return redirect('listar_tratamientos')
    else:
        form = TratamientoForm(instance=tratamiento)
    return render(request, 'editar_tratamiento.html', {'form': form, 'tratamiento': tratamiento})

# Eliminar un tratamiento
def eliminar_tratamiento(request, tratamiento_id):
    tratamiento = get_object_or_404(Tratamiento, id=tratamiento_id)
    if request.method == 'POST':
        tratamiento.delete()
    return redirect('listar_tratamientos')

def historial_tratamientos(request):
    # Obtener todas las historias clínicas por defecto
    historias_clinicas = HistoriaClinica.objects.all()

    # Crear el formulario
    form = TratamientoFilterForm(request.GET)

    # Si el formulario es válido, aplicar los filtros
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        fecha_inicio = form.cleaned_data['fecha_inicio']
        fecha_fin = form.cleaned_data['fecha_fin']

        # Aplicar los filtros si es necesario
        if nombre:
            historias_clinicas = historias_clinicas.filter(tratamiento__nombre=nombre)
        if fecha_inicio:
            historias_clinicas = historias_clinicas.filter(fecha_aplicacion_tratamiento__gte=fecha_inicio)
        if fecha_fin:
            historias_clinicas = historias_clinicas.filter(fecha_aplicacion_tratamiento__lte=fecha_fin)

    # Renderizar la plantilla
    return render(request, 'historial_tratamientos.html', {
        'historias_clinicas': historias_clinicas,
        'form': form
    })