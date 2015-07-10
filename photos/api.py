#-*- coding: utf-8 -*-
__author__ = 'arodriguez'

from photos.models import Photo
from photos.views import PhotosQuerySet
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class PhotoListApi(ListCreateAPIView, PhotosQuerySet):

    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):

        """Dependiendo de si la petición es GET o Post cambiar el serializador. Esto se hace
        pq cuando se muestra el list, no hay necesidad de mostrar todos los atributos de la photo,
        mientras que cuando se hace el POST (que es cuando se crea una foto) si se necesita mandar todos los datos
        """
        return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer

    def get_queryset(self):

        #implementar las politicas de queryset para mostrar fotos
        return self.get_photos_queryset(self.request)


class PhotoDetailApi(RetrieveUpdateDestroyAPIView, PhotosQuerySet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):

        #implementar las politicas de queryset para mostrar fotos
        return self.get_photos_queryset(self.request)
