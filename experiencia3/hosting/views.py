from django.shortcuts import redirect, render
from .models import Categoria, Cliente

# Create your views here.
def index(request):
    return render (request, 'index.html')

def galeria(request):
    return render (request, 'galeria.html')

def buscarClientes(request):
    
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', context={'datos': clientes})