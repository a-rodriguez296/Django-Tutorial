#-*- coding: utf-8 -*-
from django import forms
from photos.models import Photo
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):

        #Valida si en la descripción se han puesto malas palabras

        #Con el metodo clean se le hace clean a todos los datos del formulario
        cleaned_data = super(PhotoForm, self).clean()

        #traer description
        description = cleaned_data.get('description', '').lower()

        for badword in BADWORDS:
            if badword.lower() in description:
                #se pone la u delante para que el string sea visto como unicode
                raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

        return cleaned_data
