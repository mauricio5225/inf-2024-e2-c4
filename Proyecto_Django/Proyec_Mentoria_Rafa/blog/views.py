from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("HOLA GENTE DEL INFO2024")# DEVUELVE EN EL SERVER EL SALUDO
