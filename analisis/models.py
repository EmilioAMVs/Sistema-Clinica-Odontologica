from django.db import models
from pacientes.models import Paciente
from tratamientos.models import Tratamiento

class CasoHistorico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    sintomas = models.TextField()  # Almacena una lista de síntomas en formato de texto
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    frecuencia_prescripcion = models.IntegerField(default=0)
    resultado_exitoso = models.IntegerField(default=0)  # Número de casos con resultado positivo

    def __str__(self):
        return f'Caso de {self.paciente}'

class Recomendacion(models.Model):
    caso_historico = models.ForeignKey(CasoHistorico, on_delete=models.CASCADE)
    tratamiento_recomendado = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    porcentaje_exito = models.FloatField()
    fecha_generacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Recomendación {self.tratamiento_recomendado} - {self.porcentaje_exito}% éxito'
