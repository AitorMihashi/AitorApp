'''
Created on 3/9/2014
    
@author: pedro
'''
from django.db import models
import datetime


class Serie(models.Model):
    updated = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.updated = datetime.datetime.today()
        return super(Serie, self).save(*args, **kwargs)
    
    def __unicode__(self):
       return self.titulo
   

class Personaje(models.Model):
    updated = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=1000)
    descripcionEng = models.CharField(max_length=1000)
    serie = models.ForeignKey(Serie)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.updated = datetime.datetime.today()
        return super(Personaje, self).save(*args, **kwargs)
    
    def __unicode__(self):
       return self.nombre