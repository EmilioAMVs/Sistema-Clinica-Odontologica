from django.db import models
from django.contrib.auth.models import User  # Suponiendo que User representa al doctor

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
    hcl = models.CharField(max_length=10, unique=True, default='')  # Número de Historia Clínica (HCL)
    doctor_actual = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pacientes_actuales')
    doctor_derivado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='pacientes_derivados')
    tratamiento = models.TextField(blank=True, null=True)  # Tratamiento inicial, si es necesario

    def __str__(self):
        return f'{self.nombre} {self.apellido} (HCL: {self.hcl})'
