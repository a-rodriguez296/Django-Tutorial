#-*- coding: utf-8 -*-
__author__ = 'arodriguez'

from rest_framework.views import APIView
from photos.models import Photo
from photos.serializers import PhotoSerializer
from rest_framework.response import Response

class PhotoListApi(APIView):

    def get(self, request):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)