from django.db import models

# Create your models here.
class Autor(models.Model):
    Nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name="NOMBRE")
    Apellido = models.CharField(max_length=100, blank=False, null=False, verbose_name="APELLIDO")
    email = models.EmailField(verbose_name="Email", blank=False, null=False)
    Biografia = models.TextField(verbose_name="Biografía del Autor")
    
    def __str__(self):
        return f"{self.Nombre}{self.Apellido}"
    
    
