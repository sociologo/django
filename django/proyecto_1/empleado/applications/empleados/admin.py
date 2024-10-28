from django.contrib import admin # type: ignore
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id'
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    # buscador
    search_fields = ('first_name',)
    # filtros
    list_filter = ('departamento', 'job', 'habilidades' )
    # interfaz de seleccion
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)