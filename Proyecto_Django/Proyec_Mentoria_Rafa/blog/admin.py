from django.contrib import admin
from .models import Autor

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ("Nombre", "Apellido", "email", "Biografia")

# Registramos el modelo Autor con la configuración de AutorAdmin
admin.site.register(Autor, AutorAdmin)



