# pacientes/forms.py
from django import forms
from .models import Paciente, HistoriaClinica

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'edad', 'genero', 'direccion', 'telefono', 'email']  # Asegúrate de que los campos coincidan con el modelo

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['sintomas', 'observaciones']  # Puedes incluir otros campos si es necesario

