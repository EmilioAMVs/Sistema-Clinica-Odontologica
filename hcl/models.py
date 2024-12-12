from django.db import models
from pacientes.models import Paciente  # Importa el modelo Paciente
from usuarios.models import Usuario    # Importa el modelo Usuario (Doctor)
from tratamientos.models import Tratamiento  # Importa el modelo Tratamiento

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='historias_clinicas')
    doctor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, limit_choices_to={'rol__nombre': 'doctor'})
    diagnostico = models.TextField()
    sintomas = models.TextField()
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_aplicacion_tratamiento = models.DateField(null=True, blank=True)
    resultado_exitoso = models.BooleanField(default=False)  # Indica si el tratamiento fue exitoso
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historia Clínica de {self.paciente.nombre} - {self.fecha_creacion.strftime('%d/%m/%Y')}"

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Historia Clínica'
        verbose_name_plural = 'Historias Clínicas'
    