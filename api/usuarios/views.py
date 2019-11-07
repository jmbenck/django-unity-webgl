from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from api.forms import UsuarioForm
from .models import Cidade, Escola, Usuario
from .serializers import UsuarioSerializer, CidadeSerializer, EscolaSerializer


class UsuarioView(viewsets.ModelViewSet):
    #queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'idade']
    queryset = Usuario.objects.all()


class CidadeView(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class EscolaView(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

def ranking(request, *args, **kwargs):
    ranking = Usuario.objects.order_by('-pontuacao')
    context = {"ranking": ranking}
    return render(request, "ranking.html", context)

def usuario_cadastro(response, *args, **kwargs):
    form = UsuarioForm()
    if response.method == "POST":
        form = UsuarioForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(response, "usuario_cadastro.html", {"form":form})


