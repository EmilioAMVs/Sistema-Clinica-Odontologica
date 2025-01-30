from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Paciente
from usuarios.models import Usuario
from hcl.models import HistoriaClinica  
from .forms import PacienteCreationForm, PacienteEditForm
from clinica.decorators import role_required
from .services import PacienteService

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
@role_required(['admin', 'doctor'])
def crear_paciente(request):
    if request.method == 'GET':
        return render(request, 'crear_paciente.html', {'form': PacienteCreationForm()})
    else:
        form = PacienteCreationForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.hcl = PacienteService.generar_hcl()  # Asignar HCL antes de guardar
            doctor = Usuario.objects.get(user=request.user)
            paciente.save()

            # Crear la historia clínica asociada al paciente
            HistoriaClinica.objects.create(
                paciente=paciente,
                doctor=doctor,
                diagnostico="Diagnóstico inicial pendiente",
                sintomas="Síntomas no especificados"
            )

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
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, 'Paciente eliminado exitosamente.')
    return redirect('listar_pacientes')

# Vista de detalle para un paciente, accesible tanto para doctores como para ayudantes
@role_required(['admin','doctor','ayudante'])
def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    historias_clinicas = HistoriaClinica.objects.filter(paciente=paciente)
    
    context = {
        'paciente': paciente,
        'nombre': paciente.nombre,
        'apellido': paciente.apellido,
        'edad': paciente.edad,
        'direccion': paciente.direccion,
        'telefono': paciente.telefono,
        'email': paciente.email,
        'doctor_asignado': paciente.doctor_actual,                                                                                                                              
        'hcl': paciente.hcl,
        'historias_clinicas': historias_clinicas
    }
    return render(request, 'detalle_paciente.html', context)
