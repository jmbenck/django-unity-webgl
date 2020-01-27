import csv
from django.contrib import admin
from .models import Usuario, Escola, Cidade, Convidado

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Exportar CSV"


class EscolaAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ['escola']
    list_display = ['escola', 'cidade']
    list_filter = ['cidade']
    ordering = ['escola']
    actions = ["export_as_csv"]


class UsuarioAdmin(admin.ModelAdmin, ExportCsvMixin):
    fields = ('username', 'nome', 'idade', 'sexo', 'serie', 'cidade', 'escola',)
    list_display = ['username', 'nome', 'idade', 'sexo', 'serie', 'cidade', 'escola',]
    list_filter = ['cidade', 'escola', 'serie', 'sexo', 'idade']
    autocomplete_fields = ['escola', 'cidade']
    exclude = ['pontuacao']
    actions = ["export_as_csv"]


class CidadeAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ['cidade']
    ordering = ['cidade']
    actions = ["export_as_csv"]

class ConvidadoAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ['nome']
    list_display = ['nome', 'idade', 'sexo', 'cidade']
    list_filter = ['cidade', 'idade']
    actions = ["export_as_csv"]


admin.site.register(Escola, EscolaAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Convidado, ConvidadoAdmin)
