# analisis/forms.py
from django import forms
from .models import CasoHistorico, Recomendacion

class CasoHistoricoForm(forms.ModelForm):
    class Meta:
        model = CasoHistorico
        fields = ['paciente', 'edad', 'genero', 'sintomas', 'tratamiento', 'frecuencia_prescripcion', 'resultado_exitoso']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paciente'].label = "Paciente"
        self.fields['edad'].label = "Edad"
        self.fields['genero'].label = "Género"
        self.fields['sintomas'].label = "Síntomas"
        self.fields['tratamiento'].label = "Tratamiento"
        self.fields['frecuencia_prescripcion'].label = "Frecuencia de Prescripción"
        self.fields['resultado_exitoso'].label = "Resultado Exitoso"

class RecomendacionForm(forms.ModelForm):
    class Meta:
        model = Recomendacion
        fields = ['caso_historico', 'tratamiento_recomendado', 'porcentaje_exito']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['caso_historico'].label = "Caso Histórico"
        self.fields['tratamiento_recomendado'].label = "Tratamiento Recomendado"
        self.fields['porcentaje_exito'].label = "Porcentaje de Éxito"
