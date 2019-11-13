from django.contrib.auth.forms import UserCreationForm

from usuarios.models import Usuario


class UsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'nome', 'idade', 'sexo', 'cidade', 'escola', 'serie']