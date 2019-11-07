from django.contrib import admin
from .models import Usuario, Escola, Cidade

class EscolaAdmin(admin.ModelAdmin):
    search_fields = ['escola']
    ordering = ['escola']

class UsuarioAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'nome', 'idade', 'sexo', 'serie', 'cidade', 'escola',)
    autocomplete_fields = ['escola']
    exclude = ['pontuacao']

admin.site.register(Escola, EscolaAdmin)
admin.site.register(Cidade)
admin.site.register(Usuario, UsuarioAdmin)
