from django.db import models

# Create your models here.
class Persona(models.Model):  # aplico una herencia
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_alta = models.DateField("Fecha de Publicación")
    fecha_nacimiento = models.DateField("Fecha de Nacimiento", default='1951-01-01')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    
    