from django.shortcuts import render, redirect

from src import settings

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'



from usuarios.forms import UsuarioForm, ConvidadoForm
from .models import Cidade, Escola, Usuario


def ranking(request, *args, **kwargs):
    ranking = Usuario.objects.order_by('-pontuacao')
    context = {"ranking": ranking}
    return render(request, "ranking.html", context)

def final(request, *args, **kwargs):
    ranking = Usuario.objects.order_by('-pontuacao')
    context = {"ranking": ranking}
    return render(request, "final.html", context)

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

            return redirect("/game/")
    else:
        form = UsuarioForm()
    return render(response, "usuario_cadastro.html", {"form": form})

def convidado_cadastro(response, *args, **kwargs):
    form_convidado = ConvidadoForm()
    if response.method == "POST":
        form_convidado = ConvidadoForm(response.POST)
        if form_convidado.is_valid():
            form_convidado.save()

            return redirect("/game/")
    else:
        form = UsuarioForm()
    return render(response, "convidado_cadastro.html", {"form_convidado": form_convidado})
