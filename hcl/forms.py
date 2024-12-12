from django import forms
from .models import HistoriaClinica
from pacientes.models import Paciente  # Asegúrate de que el modelo Paciente esté disponible en el form
from usuarios.models import Usuario    # Asegúrate de que el modelo Usuario esté disponible
from tratamientos.models import Tratamiento  # Asegúrate de que el modelo Tratamiento esté disponible

class HistoriaClinicaForm(forms.ModelForm):
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
    
    tratamiento = forms.ModelChoiceField(
        queryset=Tratamiento.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Tratamiento"
    )
    fecha_aplicacion_tratamiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de Aplicación"
    )
    
    resultado_exitoso = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label="Resultado exitoso",
        required=False
    )
    
    class Meta:
        model = HistoriaClinica
        fields = [   'doctor', 'diagnostico', 'sintomas', 'tratamiento', 'fecha_aplicacion_tratamiento','resultado_exitoso']

        