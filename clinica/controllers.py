from django.shortcuts import render
from .decorators import admin_required, doctor_required, assistant_required

# Pagina de inicio
def home(request):
    return render(request, 'home.html')

# Dashboard del administrador
@admin_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

#Dashboard del doctor
@doctor_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

#Dashboard del ayudante
@assistant_required
def ayudante_dashboard(request):
    return render(request, 'ayudante_dashboard.html')
