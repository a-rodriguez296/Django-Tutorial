#-*- coding: utf-8 -*-
__author__ = 'arodriguez'


from django.views.generic import View
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


class UserListAPI(View):

    def get(self, request):
        users = User.objects.all()

        #Cuando se le pasa una coleccion a serializer hay que poner many=true
        serializer = UserSerializer(users, many=True)

        serialized_users = serializer.data

        #instanciar renderizador de JSON
        renderer = JSONRenderer()

        #Convertir users a formato JSON
        json_users = renderer.render(serialized_users)

        return HttpResponse(json_users)
