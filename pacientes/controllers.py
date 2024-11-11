from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Paciente
from hcl.models import HistoriaClinica  
from .forms import PacienteCreationForm, PacienteEditForm
from clinica.decorators import role_required

def home(request):
    return render(request, 'home.html')

# Vista para listar pacientes, accesible para doctores y ayudantes
@role_required(['admin','doctor','ayudante'])
def listar_pacientes(request):
    if request.user.usuario.rol.nombre == 'doctor':
        pacientes = Paciente.objects.filter(doctor_actual=request.user)
    elif request.user.usuario.rol.nombre == 'ayudante' or request.user.usuario.rol.nombre == 'admin':
        pacientes = Paciente.objects.all()
    else:
        messages.error(request, "No tienes permiso para ver esta sección.")
        return redirect('home')

    return render(request, 'listar_pacientes.html', {'pacientes': pacientes})

# Vista para crear un nuevo paciente, accesible solo para doctores
@role_required(['admin','doctor'])
def crear_paciente(request):
    if request.method == 'GET':
        return render(request, 'crear_paciente.html', {'form': PacienteCreationForm()})
    else:
        form = PacienteCreationForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.doctor_actual = request.user
            paciente.save()
            HistoriaClinica.objects.create(paciente=paciente, doctor_required=request.user)
            messages.success(request, 'Paciente creado exitosamente.')
            return redirect('listar_pacientes')
        else:
            return render(request, 'crear_paciente.html', {
                'form': form,
                'error': 'Error en los datos. Intenta nuevamente.'
            })

# Vista para editar un paciente existente, accesible solo para doctores
@role_required(['admin','doctor'])
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    if request.method == 'GET':
        form = PacienteEditForm(instance=paciente)
        return render(request, 'editar_paciente.html', {'form': form, 'paciente': paciente})
    else:
        form = PacienteEditForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente actualizado correctamente.')
            return redirect('listar_pacientes')
        else:
            return render(request, 'editar_paciente.html', {
                'form': form,
                'paciente': paciente,
                'error': 'Error al actualizar el paciente. Intenta nuevamente.'
            })

# Vista para eliminar un paciente, accesible solo para doctores
@role_required(['admin','doctor'])
def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id, doctor_actual=request.user)
    
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente eliminado exitosamente.')
        return redirect('listar_pacientes')
    return render(request, 'eliminar_paciente.html', {'paciente': paciente})

# Vista de detalle para un paciente, accesible tanto para doctores como para ayudantes
@role_required(['admin','doctor','ayudante'])
def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    context = {
        'paciente': paciente,
        'nombre': paciente.nombre,
        'apellido': paciente.apellido,
        'edad': paciente.edad,
        'direccion': paciente.direccion,
        'telefono': paciente.telefono,
        'email': paciente.email,
        'doctor_asignado': paciente.doctor_actual                                                                                                                              ,
        'tratamiento': paciente.tratamiento,
        'hcl': paciente.hcl
    }
    return render(request, 'detalle_paciente.html', context)
