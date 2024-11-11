from django import forms
from .models import Paciente

class PacienteCreationForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'edad', 'genero', 'direccion', 'telefono', 'email', 'hcl', 'tratamiento']
        widgets = {'genero': forms.Select(choices=Paciente.GENERO_CHOICES)}

class PacienteEditForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'edad', 'genero', 'direccion', 'telefono', 'email', 'tratamiento']
        widgets = {'genero': forms.Select(choices=Paciente.GENERO_CHOICES)}
