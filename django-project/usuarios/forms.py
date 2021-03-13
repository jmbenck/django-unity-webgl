from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario, Convidado


class UsuarioForm(UserCreationForm):

    error_css_class = "text-light bg-danger"

    class Meta:
        model = Usuario
        fields = ['username', 'nome', 'idade', 'sexo', 'cidade', 'escola', 'serie']

class ConvidadoForm(UserCreationForm):

    error_css_class = "text-light bg-danger"

    class Meta:
        model = Convidado
        fields = ['username','nome', 'idade', 'sexo', 'cidade']