#-*- coding: utf-8 -*-
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

__author__ = 'arodriguez'

def badwords_validator(value):

    #Esta funcion valida si en 'value' se han puesto malas palabras
    for badword in BADWORDS:
        if badword.lower() in value.lower():
            #se pone la u delante para que el string sea visto como unicode
            raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

    return True

