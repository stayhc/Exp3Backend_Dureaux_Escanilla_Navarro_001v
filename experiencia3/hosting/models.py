from django.db import models

# Create your models here.

class Categoria(models.Model):

    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoría')

    def __str__(self):
        return self.nombreCategoria


class Cliente(models.Model):

    rut= models.CharField(max_length=9, primary_key=True, verbose_name='Rut')
    nombre= models.CharField(max_length=30, verbose_name='Nombre del Cliente')
    tcredito = models.CharField(max_length=20, verbose_name='Numero de tarjeta de credito')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut