from django.urls import path
from .views import crearClientes, index, galeria, clientes

urlpatterns = [
    path('', index, name="index"),
    path('galeria', galeria, name="galeria"),
    path('clientes', clientes, name="clientes"),
    path('crearClientes', crearClientes, name="crearClientes")

]