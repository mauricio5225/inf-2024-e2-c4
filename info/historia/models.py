from django.db import models

# Create your models here.
class Padron(models.Model): #aplico una herencia
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_alta = models.DateField("Fecha de Publicacíon")