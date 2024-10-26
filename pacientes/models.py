from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    sintomas = models.TextField()  # Sintomas como lista en formato texto
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Historia clínica de {self.paciente}'
