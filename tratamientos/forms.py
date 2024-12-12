from django import forms
from .models import Tratamiento

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['nombre', 'descripcion','costo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre del Tratamiento"
        self.fields['descripcion'].label = "Descripción"
        self.fields['costo'].label = "Costo"

class TratamientoFilterForm(forms.Form):
    nombre = forms.ModelChoiceField(queryset=Tratamiento.objects.all(), required=False)
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)