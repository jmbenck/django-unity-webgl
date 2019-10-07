from rest_framework import serializers
from .models import Cidade, Escola, Usuario

class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = ('id', 'url', 'cidade')

class EscolaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escola
        fields = ('id', 'url', 'escola')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'url', 'login', 'senha', 'nome', 'idade', 'sexo', 'cidade', 'escola', 'serie', 'pontuacao')