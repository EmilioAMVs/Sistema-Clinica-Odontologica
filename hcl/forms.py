# forms.py en la app hcl
from django import forms
from .models import HistoriaClinica
from pacientes.models import Paciente  # Asegúrate de que el modelo Paciente esté disponible en el form
from usuarios.models import Usuario    # Asegúrate de que el modelo Usuario esté disponible

class HistoriaClinicaForm(forms.ModelForm):
    paciente = forms.ModelChoiceField(
        queryset=Paciente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Paciente"
    )
    doctor = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(rol__nombre='doctor'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Doctor"
    )
    diagnostico = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        label="Diagnóstico"
    )
    sintomas = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), 
        label="Síntomas")

    class Meta:
        model = HistoriaClinica
        fields = ['paciente', 'doctor', 'diagnostico']
