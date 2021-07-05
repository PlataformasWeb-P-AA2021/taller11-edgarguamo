from django.contrib import admin

from alquiler.models import Edificio, Departamento

class EdificioAdmin (admin.ModelAdmin):
    list_display = ('nombre', 'direccion','ciudad', 'tipo')
    search_fields = ('nombre', 'ciudad')

admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'costo_dept', 'num_cuartos', 'edificio')
    search_fields = ('nombre', 'edificio')

admin.site.register(Departamento , DepartamentoAdmin)
