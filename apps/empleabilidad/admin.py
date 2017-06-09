from django.contrib import admin
from . import models


@admin.register(models.Vacante)
class VacanteAdmin(admin.ModelAdmin):
    list_display = ['cargo',
                    'salario',
                    'fecha']


@admin.register(models.VacantePersona)
class VacantePersonaAdmin(admin.ModelAdmin):
    list_display = ['vacante',
                    'persona',
                    'fecha_contratacion',
                    'tiempo_contrato',
                    'salario',
                    'observaciones']


@admin.register(models.FormacionTrabajo)
class FormacionTrabajoAdmin(admin.ModelAdmin):
    list_display = ['fecha_creacion',
                    'nombre_programa']


@admin.register(models.FormacionTrabajoPersona)
class FormacionPersonaAdmin(admin.ModelAdmin):
    list_display = ['persona',
                    'fecha_inscripcion',
                    'tipo_formacion',
                    'estado',
                    'fecha_proceso',
                    'observacion']



