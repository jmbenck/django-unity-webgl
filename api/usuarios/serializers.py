from rest_framework import serializers
from .models import Cidade, Escola, Usuario

class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = ('url', 'id', 'cidade')

class EscolaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Escola
        fields = ('url', 'id', 'escola')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url', 'id', 'username', 'password', 'nome', 'idade', 'sexo', 'cidade', 'escola', 'serie', 'pontuacao')