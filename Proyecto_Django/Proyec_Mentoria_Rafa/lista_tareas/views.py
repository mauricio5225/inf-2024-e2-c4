from django.shortcuts import render
from .models import Tarea

# Create your views here.
def lista_tareas(request):
    tareas = Tarea.objects.all(); 
    # tareasCompletadas= Tarea.objects.filter(completada=True)
    return render(request,
                  'listaTareas.html',
                  {'tareas': tareas}
                  )
