#-*- coding: utf-8 -*-
__author__ = 'arodriguez'


from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class UserListAPI(APIView):

    def get(self, request):
        users = User.objects.all()

        #Cuando se le pasa una coleccion a serializer hay que poner many=true
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)


class UserDetailApi(APIView):

    #pq es la varialbe que me mandan desde urls
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

