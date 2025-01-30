from django import forms
from .models import HistoriaClinica
from pacientes.repositories import PacienteRepository  # Asegúrate de que el modelo Paciente esté disponible en el form
from usuarios.models import Usuario    # Asegúrate de que el modelo Usuario esté disponible
from tratamientos.models import Tratamiento  # Asegúrate de que el modelo Tratamiento esté disponible
from pacientes.decorators import formatear_paciente  # Asegúrate de que el servicio formatear_paciente esté disponible

class HistoriaClinicaForm(forms.ModelForm):
    
    paciente = forms.ModelChoiceField(
        queryset=PacienteRepository.obtener_todos(),  # Se asignará dinámicamente en __init__
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicamos el decorador a la representación del paciente en el select
        self.fields['paciente'].label_from_instance = formatear_paciente(lambda obj: obj)
    
    class Meta:
        model = HistoriaClinica
        fields = [   'paciente','doctor', 'diagnostico', 'sintomas', 'tratamiento', 'fecha_aplicacion_tratamiento','resultado_exitoso']

        