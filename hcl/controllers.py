from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Count, Q
from .models import HistoriaClinica
from .forms import HistoriaClinicaForm
from clinica.decorators import role_required
from tratamientos.models import Tratamiento

@role_required(['admin','doctor','ayudante'])
def listar_historias(request):
    historias = HistoriaClinica.objects.all()
    return render(request, 'listar_historias.html', {'historias': historias})


@role_required(['doctor'])
def crear_historia(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historia clínica creada exitosamente.')
            return redirect('listar_historias')  # Redirige a la lista de historias clínicas, o donde prefieras
        else:
            messages.error(request, 'Hubo un error al crear la historia clínica. Revisa los datos e intenta nuevamente.')
    else:
        form = HistoriaClinicaForm()

    return render(request, 'crear_historia.html', {'form': form})


@role_required(['admin','doctor'])
def editar_historia(request, historia_id):
    historia = get_object_or_404(HistoriaClinica, id=historia_id)
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST, instance=historia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historia clínica actualizada correctamente.')
            return redirect('listar_historias')
    else:
        form = HistoriaClinicaForm(instance=historia)
    return render(request, 'editar_historia.html', {'form': form, 'historia': historia})


@role_required(['admin','doctor'])
def eliminar_historia(request, historia_id):
    historia = get_object_or_404(HistoriaClinica, id=historia_id)
    if request.method == 'POST':
        historia.delete()
        messages.success(request, 'Historia clínica eliminada exitosamente.')
        return redirect('listar_historias')
    return render(request, 'eliminar_historia.html', {'historia': historia})


@role_required(['admin','doctor','ayudante'])
def detalle_historia(request, historia_id):
    historia = get_object_or_404(HistoriaClinica, id=historia_id)
    return render(request, 'detalle_historia.html', {'historia': historia})

@role_required(['admin','doctor'])
def comparar_historia(request, historia_id):
    historia_actual = get_object_or_404(HistoriaClinica, id=historia_id)

    # Obtener historias similares según edad, género, y síntomas
    historias_similares = HistoriaClinica.objects.filter(
        paciente__edad__gte=historia_actual.paciente.edad - 5,
        paciente__edad__lte=historia_actual.paciente.edad + 5,
        paciente__genero=historia_actual.paciente.genero,
        sintomas__icontains=historia_actual.sintomas  # Busca coincidencias en los síntomas
    ).exclude(id=historia_actual.id)

    # Calcular tratamientos más frecuentes y sus porcentajes de éxito
    tratamiento_stats = (
        historias_similares
        .values('tratamiento')
        .annotate(
            total=Count('id'),
            exitosos=Count('id', filter=Q(resultado_exitoso=True))
        )
        .order_by('-total')  # Ordenar por cantidad de uso
    )

    # Construir la lista de tratamientos sugeridos con porcentajes de éxito
    sugerencias = [
        {
            'tratamiento': Tratamiento.objects.get(id=stat['tratamiento']).nombre if stat['tratamiento'] else "No especificado",
            'frecuencia': stat['total'],
            'porcentaje_exito': (stat['exitosos'] / stat['total']) * 100 if stat['total'] > 0 else 0
        }
        for stat in tratamiento_stats if stat['tratamiento']    
    ]

    return render(request, 'comparar_historia.html', {
        'historia': historia_actual,
        'sugerencias': sugerencias,
    })