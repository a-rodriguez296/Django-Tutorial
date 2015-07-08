#esto es para que acepte acentos
#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from photos.settings import LICENSES



# Create your models here.

PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIBILITY = (
    (PUBLIC , 'Pública'),
    (PRIVATE, 'Privada')
)

class Photo(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __unicode__(self):
        return self.name