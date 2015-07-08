#esto es para que acepte acentos
#-*- coding: utf-8 -*-

#esto realmente son los controladores, razón por la cual acá no debe ir nada de la presentación

from django.http import *
from django.shortcuts import render
from photos.models import Photo, PUBLIC
from photos.forms import PhotoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

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


@login_required
def create(request):

    success_message = ''
    if request.method == 'GET':
        form = PhotoForm()
    elif request.method == 'POST':

        #Crea una instancia vacía de foto
        photo_with_owner = Photo()

        #Asigna los datos
        photo_with_owner.owner = request.user

        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save() #Guarda el objeto que viene en el formulario y lo devuelve

            #Poner todos los campos vacíos
            form = PhotoForm()

            success_message = 'Guardado con exito!'

            #reverse sirve para generar la url
            success_message += '<a href="{0}">'.format(reverse('photo_detail', args=[new_photo.pk]))
            success_message += 'Ver Foto'
            success_message += '</a>'
    context = {
        'form': form,
        'success_message': success_message
    }
    return render(request, 'photos/new_photo.html', context)

