from rest_framework import serializers
from .models import Usuario, Viaje

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'password', 'nombre', 'apellido', 'telefono', 'tipoDeUsuario']

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = ['id', 'dia', 'hora', 'pasajeros', 'comunaDestino', 'Precio', 'idPasajeros']