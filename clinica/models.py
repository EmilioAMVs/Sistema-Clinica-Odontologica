from django.db import models
from tratamientos.models import Tratamiento
from pacientes.models import Paciente

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='historias_clinicas_clinica')  # Cambia aquí
    fecha_creacion = models.DateField(auto_now_add=True)
    sintomas = models.TextField()  # Síntomas como lista en formato texto
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Historia clínica de {self.paciente}'

class AnalisisCaso(models.Model):
    historia_clinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    sintomas = models.TextField()
    tratamiento_recomendado = models.ForeignKey(Tratamiento, on_delete=models.CASCADE, blank=True, null=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Análisis de caso para {self.historia_clinica}'
