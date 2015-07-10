#-*- coding: utf-8 -*-
from django import forms
from photos.models import Photo
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['owner']
