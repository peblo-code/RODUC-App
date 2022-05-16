from urllib import request
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from RoducWeb.models import *
from datetime import datetime

# Create your views here.

def Auditoria(request, user, info):
    nueva_sesion = Auditoria_Sesiones(
        nombre_usuario = request.session.get(user),
        fecha = datetime.now(),
        informacion = info
    )
    nueva_sesion.save()

class UsuarioListAPIView(generics.ListAPIView):
    def Solicitud(request):
        Auditoria(request, 'Inicio Sesion')
    queryset = Usuario.objects.all()
    
    serializer_class = UsuarioListSerializer
class UsuarioRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "nombre_usuario"
    print(lookup_field)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer