#-*- coding: utf-8 -*-
from django import forms
from photos.models import Photo

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['owner']
