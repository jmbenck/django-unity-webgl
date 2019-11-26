from django.contrib import admin
from .models import Usuario, Escola, Cidade

class EscolaAdmin(admin.ModelAdmin):
    search_fields = ['escola']
    ordering = ['escola']

class UsuarioAdmin(admin.ModelAdmin):
    fields = ('username', 'nome', 'idade', 'sexo', 'serie', 'cidade', 'escola',)
    autocomplete_fields = ['escola']
    exclude = ['pontuacao']

class CidadeAdmin(admin.ModelAdmin):
    search_fields = ['cidade']


admin.site.register(Escola, EscolaAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Usuario, UsuarioAdmin)
