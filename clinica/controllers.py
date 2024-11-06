from django.shortcuts import render, redirect
from .forms import HistoriaClinicaForm, AnalisisCasoForm
from .models import HistoriaClinica, AnalisisCaso
from usuarios.models import Usuario
from .decorators import admin_required, doctor_required, assistant_required

# Vista para que solo el administrador pueda crear historias clínicas
@admin_required
@doctor_required
def crear_historia_clinica(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('listar_historias_clinicas')
    else:
        form = HistoriaClinicaForm()
    return render(request, 'crear_historia_clinica.html', {'form': form})

# Vista para que el doctor pueda crear un análisis de caso
@doctor_required
def crear_analisis_caso(request):
    if request.method == 'POST':
        form = AnalisisCasoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_analisis_casos')
    else:
        form = AnalisisCasoForm()
    return render(request, 'crear_analisis_caso.html', {'form': form})

# Vista para que el administrador pueda listar historias clínicas
@admin_required
@doctor_required
def listar_historias_clinicas(request):
    historias = HistoriaClinica.objects.all()
    return render(request, 'listar_historias_clinicas.html', {'historias': historias})

# Vista para que el doctor o asistente puedan listar análisis de casos
@doctor_required
@assistant_required
def listar_analisis_casos(request):
    analisis_casos = AnalisisCaso.objects.all()
    return render(request, 'listar_analisis_casos.html', {'analisis_casos': analisis_casos})

# Dashboard del administrador
@admin_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@doctor_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

@assistant_required
def asistente_dashboard(request):
    return render(request, 'assistant_dashboard.html')
