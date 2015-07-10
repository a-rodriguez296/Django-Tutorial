__author__ = 'arodriguez'

from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene permiso para realizar la accion
        (GET, POST, PUT, DELETE)
        :param request:
        :param view:
        :return:
        """
        #Este import se hace acá pq si se pone el la cabecera se crea una dependencia ciclica
        from users.api import UserDetailApi

        #Caso de crear un usuario -> Cualquiera lo puede crear entonces True
        if request.method=="POST":
            return True
        elif request.user.is_superuser:
            return True

        #Si es un get a la vista de detalle, tomo la decision en has_object_permission
        elif isinstance(view, UserDetailApi):
            return True
        else:
            #este es el caso de un get del listado
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado tiene permisos para realizar la accion (GET, POST, PUT, DELETE)
         sobre el objeto obj
        :param request:
        :param view:
        :param obj:
        :return:
        """
        #Dada la clase anterior, acá solo van a llegar las peticiones GET, PUT, o DELETE
        # si es super user puede hacer lo que quiera, sino un usuario puede editar o ver el detalla de lo suyo
        return request.user.is_superuser or request.user == obj