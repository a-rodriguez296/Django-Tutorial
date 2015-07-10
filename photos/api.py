#-*- coding: utf-8 -*-
__author__ = 'arodriguez'

from rest_framework.views import APIView
from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class PhotoListApi(ListCreateAPIView):

    queryset = Photo.objects.all()

    def get_serializer_class(self):

        """Dependiendo de si la petición es GET o Post cambiar el serializador. Esto se hace
        pq cuando se muestra el list, no hay necesidad de mostrar todos los atributos de la photo,
        mientras que cuando se hace el POST (que es cuando se crea una foto) si se necesita mandar todos los datos
        """
        return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer


class PhotoDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
