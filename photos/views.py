#esto es para que acepte acentos
#-*- coding: utf-8 -*-
#esto realmente son los controladores, razón por la cual acá no debe ir nada de la presentación


from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

# Create your views here.

def home(request):
    photos = Photo.objects.all()
    html = '<ul>'
    for photo in photos:
        html += '<li>' + photo.name + '</li>'
    html +='</ul>'

    return HttpResponse(html)
