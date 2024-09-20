from django.shortcuts import render
from django.http import HttpResponse
# GET
# POST
# DELETE
# PUT


# Create your views here.
def index(request):
    return HttpResponse("Hola mundo desde la web")
