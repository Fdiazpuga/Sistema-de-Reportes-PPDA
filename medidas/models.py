from django.db import models

class Medida(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(
        max_length=50,
        choices=[('Regulatoria', 'Regulatoria'), ('No Regulatoria', 'No Regulatoria'), ('Difusión', 'Difusión')]
    )
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    medida = models.ForeignKey('Medida', on_delete=models.CASCADE, related_name='actividades')
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return f"{self.medida.nombre} - {self.descripcion[:20]}"