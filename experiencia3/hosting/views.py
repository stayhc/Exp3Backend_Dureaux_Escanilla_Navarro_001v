from django.shortcuts import redirect, render
from .models import Categoria, Cliente
from .forms import ClienteForm

# Create your views here.
def index(request):
    return render (request, 'index.html')

def galeria(request):
    return render (request, 'galeria.html')

def clientes(request):
    
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', context={'datos': clientes})

def crearClientes(request):
    if request.method=='POST':
        cliente=ClienteForm(request.POST)
        if cliente.is_valid():
            cliente.save()
            return redirect('clientes')
    else:
        cliente=ClienteForm()
    return render(request, 'hosting/form_crearcliente.html', {'cliente': cliente})