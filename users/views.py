#-*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login

# Create your views here.


def login(request):

    error_messages = []

    if request.method == 'POST':

        #forma segura de acceder a claves en un diccionario. Nunca acceder a un diccionario con la sintaxis de corchetes. POST['usr']
        username = request.POST.get('usr')
        password = request.POST.get('pwd')

        user = authenticate (username = username, password = password)

        if user is None:
            error_messages.append('Nombre de usuario o contraseña incorrecto')
        else:
            if user.is_active:
                django_login(request, user)
                return redirect('photos_home')
            else:
                error_messages.append('El usuario no esta activo')

    context = {
        'errors' : error_messages
    }
    return render(request, 'users/login.html', context)


def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('photos_home')