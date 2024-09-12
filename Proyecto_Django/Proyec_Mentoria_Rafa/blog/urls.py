
from django.urls import path
from .views import saludo # importo desde blog.views saludo

urlpatterns = [   
    path('', saludo)
]