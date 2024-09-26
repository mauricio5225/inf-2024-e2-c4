from django.urls import path
from . import views

urlpatterns = [
    path('', views.historia_elecciones, name='historia_elecciones'),
]


