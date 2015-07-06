#esto es para que acepte acentos
#-*- coding: utf-8 -*-

#esto realmente son los controladores, razón por la cual acá no debe ir nada de la presentación

from django.http import *
from django.shortcuts import render
from photos.models import Photo, PUBLIC

# Create your views here.

def home(request):
    photos = Photo.objects.filter(visibility = PUBLIC).order_by('-created_at')
    # trae solo las primeras dos fotos
    context = {'photos_list': photos[:2]}
    return render(request, 'photos/home.html', context)

def detail(request, pk):
    # Carga el detalle de una foto
    possible_photos = Photo.objects.filter( id = pk)

    # photo = len(possible_photos) == 1 ? possible_photos[0] : None
    photo = possible_photos[0] if len(possible_photos) == 1 else None

    if photo is not None:
        #Cargar l plantilla de detalla
        context = {'photo' : photo}
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound("No existe dicha foto")