from django import forms
from .models import Tratamiento, AplicacionTratamiento

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['nombre', 'descripcion', 'costo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre del Tratamiento"
        self.fields['descripcion'].label = "Descripción"
        self.fields['costo'].label = "Costo"

class AplicacionTratamientoForm(forms.ModelForm):
    class Meta:
        model = AplicacionTratamiento
        fields = ['paciente', 'tratamiento', 'observaciones']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paciente'].label = "Paciente"
        self.fields['tratamiento'].label = "Tratamiento"
        self.fields['observaciones'].label = "Observaciones"
