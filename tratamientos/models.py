from django.db import models

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=8, decimal_places=2,null=True)

    def __str__(self):
        return self.nombre