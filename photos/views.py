#esto es para que acepte acentos
#-*- coding: utf-8 -*-
#esto realmente son los controladores, razón por la cual acá no debe ir nada de la presentación


from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

# Create your views here.

def home(request):
    photos = Photo.objects.all()
    # trae solo las primeras dos fotos
    context ={'photos_list': photos[:2]}
    return render(request, 'photos/home.html', context)
