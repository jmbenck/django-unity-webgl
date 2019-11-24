from django.shortcuts import render, redirect

from src import settings

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'



from usuarios.forms import UsuarioForm
from .models import Cidade, Escola, Usuario


def ranking(request, *args, **kwargs):
    ranking = Usuario.objects.order_by('-pontuacao')
    context = {"ranking": ranking}
    return render(request, "ranking.html", context)

def game(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, "index.html")


def usuario_cadastro(response, *args, **kwargs):
    form = UsuarioForm()
    if response.method == "POST":
        form = UsuarioForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(response, "usuario_cadastro.html", {"form": form})
