#-*- coding: utf-8 -*-
__author__ = 'arodriguez'

from rest_framework import serializers
from models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
