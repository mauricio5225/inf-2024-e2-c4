from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título', null=False)
    descripcion = models.TextField(verbose_name='Descripción', null= True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.titulo
    