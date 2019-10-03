from django.contrib import admin
from .models import  Usuario, Escola, Cidade

admin.site.register(Escola)
admin.site.register(Cidade)
admin.site.register(Usuario)
