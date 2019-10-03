from django.db import models

sexo = (
    ('1', 'Masculino'),
    ('2', 'Feminino'),
)

serie = (
    ('1', '1ª Ano'),
    ('2', '2ª Ano'),
    ('3', '3ª Ano'),
    ('4', '4ª Ano'),
    ('5', '5ª Ano'),
    ('6', '6ª Ano'),
    ('7', '7ª Ano'),
    ('8', '8ª Ano'),
    ('9', '9º Ano'),
)
class Cidade(models.Model):
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=40)

class Escola(models.Model):
    escola = models.CharField(max_length=50)
    cidade = models.ForeignKey('Cidade', models.DO_NOTHING, blank=True, null=True)

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo = models.IntegerField(choices=sexo, unique=True)
    serie = models.CharField(max_length=20, choices=serie, unique=True)
    cidade = models.ForeignKey('Cidade', models.DO_NOTHING, blank=True, null=True)
    escola = models.ForeignKey('Escola', models.DO_NOTHING, blank=True, null=True)
    pontuacao = models.DecimalField(decimal_places=2, max_digits=8, default=0)

