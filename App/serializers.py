'''
Created on 3/9/2014

@author: pedro
'''
from django.forms import widgets
from rest_framework import serializers
from App.models import Personaje, Serie
    

class PersonajeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Personaje
        fields = ('id','updated','nombre','fecha','descripcion','serie')

class PersonajeEngSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Personaje
        fields = ('id','updated','nombre','fecha','descripcionEng','serie')
    
class SerieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Serie
        fields = ('id','updated','titulo')
    