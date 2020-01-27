from django.contrib.auth.models import User
from django.db import models

sexo = [
    (1, 'Masculino'),
    (2, 'Feminino'),
]

serie = [
    (1, '1º Ano'),
    (2, '2º Ano'),
    (3, '3º Ano'),
    (4, '4º Ano'),
    (5, '5º Ano'),
    (6, '6º Ano'),
    (7, '7º Ano'),
    (8, '8º Ano'),
    (9, '9º Ano'),
]


class Cidade(models.Model):
    cidade = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.cidade

    class Meta:
        ordering = ['cidade']


class Escola(models.Model):
    escola = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING)
    def __str__(self):
        return self.escola

    class Meta:
        ordering = ['escola']


class Usuario(User):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo = models.IntegerField(choices=sexo)
    serie = models.IntegerField(choices=serie)
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING)
    escola = models.ForeignKey(Escola, models.DO_NOTHING)
    pontuacao = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Usuario'

class Convidado(User):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo = models.IntegerField(choices=sexo)
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING)

    def __str__(self):
        return self.nome
