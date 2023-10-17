from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128) 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    tipoDeUsuario = models.CharField(max_length=15, default='Pasajero')

class Viaje(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.DateField()
    hora = models.TimeField()
    pasajeros = models.IntegerField()
    comunaDestino = models.CharField(max_length=100)
    Precio = models.IntegerField()
    idPasajeros = models.CharField(max_length=50)