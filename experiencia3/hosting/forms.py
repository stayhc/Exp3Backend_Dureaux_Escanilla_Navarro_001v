from django import forms
from django.forms import ModelForm, widgets
from .models import Cliente, Categoria

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'email', 'categoria']

        labels={
            'rut': 'Rut',
            'nombre': 'Nombre', 
            'apellido': 'Apellido', 
            'email': 'Email',
            'categoria': 'Categoria',
        }

        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su rut', 
                    'id': 'rut'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre', 
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su apellido', 
                    'id': 'apellido'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su Email', 
                    'id': 'email'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            )
        }