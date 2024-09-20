from django.shortcuts import render
from django.http import HttpResponse
# GET
# POST
# DELETE
# PUT

from .models import Persona
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo desde la web")

# creo otra vista
def persona_id(request, id_persona):
    response = "La persona con id: es %s"
    return HttpResponse(response % id_persona)

def personas_list(request):
    personas_list = Persona.objects.all()
    print(personas_list)
    return HttpResponse(personas_list)

def personas_template(request):
    personas_list = Persona.objects.all()
    template = loader.get_template("personas_template.html")
    context = {"personas_list": personas_list, "title":"INFORMATORIO"  }
    return HttpResponse(template.render(context, request))
