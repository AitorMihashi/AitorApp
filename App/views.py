'''
Created on 3/9/2014

@author: pedro
'''
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from App.models import Personaje, Serie
from App.serializers import PersonajeSerializer, SerieSerializer, PersonajeEngSerializer
from django.views.decorators.csrf import csrf_exempt

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def Series_list(request):
    print "log 1"
    if request.method == 'GET':
        print "log 7"
        serie = Serie.objects.all()
        serializer = SerieSerializer(serie, many=True) 
        personaje = Personaje.objects.all()
        pserializer=None
        if 'eng' in request.GET:
            pserializer = PersonajeEngSerializer(personaje, many=True)
        else:
            pserializer = PersonajeSerializer(personaje, many=True)
        return JSONResponse(serializer.data + pserializer.data)

    elif request.method == 'POST':
        try:
            print "log 8"
            print "---" + request.POST['updated']
            serie = Serie.objects.filter(updated__gt = request.POST['updated'])
            print "log 9"
            personaje = Personaje.objects.filter(updated__gt = request.POST['updated'])
            
            pserializer=None
            print "log 2"
            if 'eng' in request.POST:
                print "log 3"
                pserializer = PersonajeEngSerializer(personaje, many=True)
                print "log 4"
            else:
                print "log 5"
                pserializer = PersonajeSerializer(personaje, many=True)
                print "log 6"
            serializer = SerieSerializer(serie, many=True)

            return JSONResponse(serializer.data + pserializer.data)

        except Exception, e:
            print e
            return JSONResponse(status=400)
