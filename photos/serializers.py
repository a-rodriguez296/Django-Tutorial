#-*- coding: utf-8 -*-
__author__ = 'arodriguez'

from rest_framework import serializers
from models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo


class PhotoListSerializer(PhotoSerializer):

    #Para que se herede la clase Meta hay que hacer esto.
    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name','url')
