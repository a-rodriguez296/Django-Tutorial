#-*- coding: utf-8 -*-
__author__ = 'arodriguez'


from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from users.permissions import UserPermission
from rest_framework.generics import GenericAPIView


class UserListAPI(GenericAPIView):

    #HAciendo esto logro que se ejecute has_permissions
    permission_classes = (UserPermission, )

    def get(self, request):
        users = User.objects.all()

        #Cuando se le pasa una coleccion a serializer hay que poner many=true
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailApi(GenericAPIView):

    """
    Para hacer que se ejecute
    #has_object_permission debo hacerlo en cada metodo (def get, def put, etc)
    permission_classes = (UserPermission, ) dado que yo he implementado estas clases.
    En otras palabras, si yo implemento el get, put y delete me toca hacerlo
    """
    permission_classes = (UserPermission, )

    #pq es la varialbe que me mandan desde urls
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(User, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)