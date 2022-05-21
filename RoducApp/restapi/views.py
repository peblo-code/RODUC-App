from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from RoducWeb.models import *
from datetime import datetime
from django.core import serializers

#################################################################
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
###########
#Auditoria Sesion
def auditar_sesion(request, user, info):
    nueva_sesion = Auditoria_Sesiones(
        nombre_usuario = user,
        fecha = datetime.now(),
        informacion = "Inicio de Sesion en " + info
    )
    nueva_sesion.save()

class UsuarioListAPIView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer
    
class UsuarioRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "nombre_usuario"
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer

class FacultadListAPIView(generics.ListAPIView):
    queryset = Facultad.objects.all()
    serializer_class = FacultadListSerializer

class FacultadRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "cod_facultad"
    queryset = Facultad.objects.all()
    serializer_class = FacultadListSerializer

#FUNCIONES
def validarSesion(request, user):
    if request.method == 'GET':
        if Usuario_Rol.objects.filter(estado = 1, cod_usuario = user, cod_rol_usuario = 2).exists():
            return JsonResponse({"respuesta": 1})
        else:
            return JsonResponse({"respuesta": 0})
@csrf_exempt
def auditoriaSesion(request, user, info):
    if request.method == "GET":
        auditar_sesion(request, user, info)
        return JsonResponse({"bandera": 1})
    else:
        print("No entro a get")
        return JsonResponse({"bandera": 0})
    

