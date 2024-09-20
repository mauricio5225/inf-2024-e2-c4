from django.contrib import admin
from .models import autor

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display=("Nombre","Apellido","Email","Biografia")
    
    pass 
        
    #(clase que esta en models.py que esta en admin.py)
    

admin.site.register(Autor, AutorAdmin)

"""    
# corregido. ojo
from django.contrib import admin
from .models import Autor

class AutorAdmin(admin.ModelAdmin):
    # Your admin configurations here
    pass

admin.site.register(Autor, AutorAdmin)"""

    