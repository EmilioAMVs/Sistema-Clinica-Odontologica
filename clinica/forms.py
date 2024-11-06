from django import forms
from .models import HistoriaClinica, AnalisisCaso

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'observaciones']

class AnalisisCasoForm(forms.ModelForm):
    class Meta:
        model = AnalisisCaso
        fields = ['historia_clinica', 'edad', 'genero', 'sintomas', 'tratamiento_recomendado']
