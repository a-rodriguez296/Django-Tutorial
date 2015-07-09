#-*- coding: utf-8 -*-
__author__ = 'arodriguez'

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    #Un Serializador debe definir 2 métodos obligatoriamente, create y update

    def create(self, validated_data):

        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):

        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        #Esto se hace para encriptar la contraseña
        instance.set_password(validated_data.get('password'))

        #Guardar en la base de datos
        instance.save()

        return instance

    #como se usa validate+campo en data ya viene el valor. Si solo fuera validate vendría  to do en un diccionario.
    def validate_username(self, data):

        users = User.objects.filter(username=data)

        #Si estoy creando un usuario (self.instance)= NONE y existe un usuario con ese username-> lanzar excepcion
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        #Si estoy actualizando un usuario y el nombre de usuario ya existen
        elif self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        else:
            return data