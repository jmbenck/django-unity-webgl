from rest_framework import viewsets
from rest_framework.response import Response
from usuarios.models import Usuario, Cidade, Escola
from .serializers import UsuarioSerializer, CidadeSerializer, EscolaSerializer
from django_filters import rest_framework as filters


class UsuarioFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')
    cidade = filters.CharFilter(lookup_expr='icontains')
    escola = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Usuario
        fields = ('nome', 'cidade', 'escola')


class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filterset_class = UsuarioFilter


class CidadeView(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer




class EscolaView(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
    filter_fields = ('cidade',)
