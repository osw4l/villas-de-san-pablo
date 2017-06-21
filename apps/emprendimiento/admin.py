from django.contrib import admin
from . import models


# Register your models here.


class BaseNameBusinessAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'negocios']


class BaseNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(models.TipoNegocio)
class TipoNegocioAdmin(BaseNameBusinessAdmin):
    pass


@admin.register(models.TipoUnidadProductiva)
class TipoUnidadProductivaAdmin(BaseNameAdmin):
    pass


@admin.register(models.Sector)
class SectorAdmin(BaseNameAdmin):
    pass


@admin.register(models.Negocio)
class NegocioAdmin(BaseNameAdmin):
    list_display = ['id', 'nombre', 'direccion', 'propietario', 'tipo_negocio']


@admin.register(models.Empresa)
class EmpresaAdmin(BaseNameAdmin):
    pass


@admin.register(models.Emprendimiento)
class EmprendimientoAdmin(admin.ModelAdmin):
    list_display = ['id', 'persona', 'tipo_negocio', 'negocio', 'ficha_caracterizacion', 'sector']


@admin.register(models.OportunidadComercial)
class OportunidadComercialAdmin(admin.ModelAdmin):
    list_display = ['id', 'negocio', 'fecha', 'empresa']


@admin.register(models.FortalecimientoEmpresarial)
class FortalecimientoEmpresarialAdmin(admin.ModelAdmin):
    list_display = ['id', 'persona', 'negocio', 'emprendimiento', 'rut', 'nit', 'camara_de_comercio']
