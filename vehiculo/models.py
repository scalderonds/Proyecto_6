from django.db import models
from django.utils import timezone

# Create your models here.


class Vehiculo(models.Model):
    MARCA_CHOICES = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]
    CATEGORIA_CHOICES = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(
        max_length=20, choices=MARCA_CHOICES, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=20, choices=CATEGORIA_CHOICES, default='Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.modelo
