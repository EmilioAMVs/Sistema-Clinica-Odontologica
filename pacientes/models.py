from django.db import models
from django.db.models import Max
from django.contrib.auth.models import User  # Suponiendo que User representa al doctor
from .services import PacienteService

class Paciente(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)  # Lista desplegable
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    hcl = models.CharField(max_length=10, unique=True, blank=False)  # Número de Historia Clínica (HCL)
    doctor_actual = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pacientes_actuales')
    doctor_derivado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='pacientes_derivados')

def save(self, *args, **kwargs):
        # Si no se asignó un HCL, generarlo automáticamente
        if not self.hcl:
            self.hcl = PacienteService.generar_hcl()
        super().save(*args, **kwargs)

def __str__(self):
        return f'{self.nombre} {self.apellido} (HCL: {self.hcl})'
