from django.shortcuts import render
from rest_framework import viewsets

from .models import Cidade, Escola, Usuario
from .serializers import UsuarioSerializer


class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
