from rest_framework import serializers
from .models import Cidade, Escola, Usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'url', 'nome', 'idade', 'sexo', 'serie', 'cidade', 'escola')