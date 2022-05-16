from urllib import request
from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from RoducWeb.models import *
from datetime import datetime

# Create your views here.

def Auditoria(info):
    nueva_sesion = Auditoria_Sesiones(
        nombre_usuario = request.sessions.get('nombre_usuario'),
        fecha = datetime.datetime.now(),
        informacion = info
    )
    nueva_sesion.save()

class UsuarioListAPIView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    Auditoria('Inicio de Sesion')
    serializer_class = UsuarioListSerializer
class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "nombre_usuario"
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer