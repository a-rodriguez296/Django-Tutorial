#-*- coding: utf-8 -*-
__author__ = 'arodriguez'

from rest_framework import serializers
from models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo

        #esto no entiendo muy bien para que es
        read_only_fields = ('owner', )


class PhotoListSerializer(PhotoSerializer):

    #Para que se herede la clase Meta hay que hacer esto.
    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')
