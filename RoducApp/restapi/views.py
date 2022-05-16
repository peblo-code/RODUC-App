from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from RoducWeb.models import *

# Create your views here.

class UsuarioListAPIView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer

class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "nombre_usuario"
    queryset = Usuario.objects.all()
    serializer_class = UsuarioDetailSerializer