from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Capacitacion)
class CapacitacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(models.HabilidadBlanda)
class HabilidadBlandaAdmin(admin.ModelAdmin):
    list_display = ['id', 'persona', 'estado_certificado', 'test', 'observaciones']
