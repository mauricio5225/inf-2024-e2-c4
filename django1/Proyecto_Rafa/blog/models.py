from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, blank=False, null=False, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Email", blank=False, null=False)
    biografia = models.TextField(verbose_name="Biografía del Autor")
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    