from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, HistoriaClinica
from .forms import PacienteForm, HistoriaClinicaForm

# Listado de pacientes
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista_pacientes.html', {'pacientes': pacientes})

# Detalle de un paciente
def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'pacientes/detalle_paciente.html', {'paciente': paciente})

# Crear un nuevo paciente
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/crear_paciente.html', {'form': form})

# Editar un paciente existente
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('detalle_paciente', paciente_id=paciente.id)
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/editar_paciente.html', {'form': form, 'paciente': paciente})

# Eliminar un paciente
def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'pacientes/eliminar_paciente.html', {'paciente': paciente})
