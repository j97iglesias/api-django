from django.shortcuts import render
from rest_framework import viewsets

from .models import Usuario, Proyecto, Tarea
from .serializer import UsuarioSerializer, ProyectoSerializer, TareaSerializer
# Create your views here.


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
