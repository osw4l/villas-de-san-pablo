from django.contrib import admin
from . import  models

# Register your models here.


@admin.register(models.GradoEscolaridad)
class GradoEscolaridadAdmin(admin.ModelAdmin):
    list_display = ['nombre_grado_escolaridad',
                    'cantidad_personas']


@admin.register(models.TituloGrado)
class TituloGradoAdmin(admin.ModelAdmin):
    list_display = ['nombre_titulo',
                    'grado_escolaridad',
                    'cantidad_personas']


@admin.register(models.TipoVivienda)
class TipoViviendaAdmin(admin.ModelAdmin):
    list_display = ['nombre_tipo_vivienda',
                    'cantidad_personas']


@admin.register(models.TipoManzana)
class TipoManzanaAdmin(admin.ModelAdmin):
    list_display = ['nombre_tipo_manzana',
                    'cantidad_personas']


@admin.register(models.Manzana)
class ManzanaAdmin(admin.ModelAdmin):
    list_display = ['numero_manzana',
                    'tipo_manzana',
                    'cantidad_personas']


@admin.register(models.Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ['numero_casa',
                    'numero_telefono',
                    'numero_telefono_2',
                    'numero_manzana',
                    'tipo_vivienda',
                    'cantidad_personas']


@admin.register(models.Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombres',
                    'apellidos',
                    'sexo',
                    'estado_civil',
                    'edad',
                    'telefono_1'
                    'telefono_2',
                    'fecha_de_registro',
                    'fecha_ingreso',
                    'tiene_empleo',
                    'origen_ingreso',
                    'ingreso_promedio_mensual',
                    'ingreso_promedio_familiares',
                    'ingreso_promedio_mensuales',
                    'vulnerabilidad',
                    'hoja_de_vida',
                    'cv_last_update',
                    'email',
                    'grado_escolaridad',
                    'titulo_grado',
                    'tipo_vivienda',
                    'tipo_manzana',
                    'manzana',
                    'casa']


@admin.register(models.TipoFormacionComplementaria)
class TipoFormacionAdmin(admin.ModelAdmin):
    list_display = ['nombre']


@admin.register(models.FormacionComplementariaPersona)
class FormacionComplementariaPersonaAdmin(admin.ModelAdmin):
    list_display = ['persona',
                    'nombre_curso',
                    'tipo_formacion']








