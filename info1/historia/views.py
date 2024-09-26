from django.shortcuts import render
from django.http import HttpResponse
# GET
# POST
# DELETE
# PUT


# Create your views here.
def historia_elecciones(request):
    return HttpResponse("Esta es la historia de las elecciones en mi provincia") 

