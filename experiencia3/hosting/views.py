from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render (request, 'index.html')

def galeria(request):
    return render (request, 'galeria.html')