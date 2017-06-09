from django.db import models
from . import constants
# Create your models here.


class Vacante(models.Model):
    cargo = models.CharField(max_length=30)
    salario = models.PositiveIntegerField()
    fecha = models.DateField()

    class Meta:
        verbose_name = 'Vacante'
        verbose_name_plural = 'Vacantes'

    def __str__(self):
        return '{} ${}, {}'.format(self.cargo, self.salario, self.fecha)


class VacantePersona(models.Model):
    vacante = models.ForeignKey(Vacante)
    persona = models.ForeignKey('personas.Persona')
    fecha_contratacion = models.DateField(
        blank=True,
        null=True
    )
    tiempo_contrato = models.CharField(
        max_length=50,
        choices=constants.TIEMPO_CONTRATO
    )
    salario = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    observaciones = models.TextField(
        blank=True,
        null=True
    )


class FormacionTrabajo(models.Model):
    fecha_creacion = models.DateField()
    nombre_programa = models.CharField(
        max_length=100
    )


class FormacionTrabajoPersona(models.Model):
    persona = models.ForeignKey('personas.Persona')
    fecha_instripcion = models.DateField()
    tipo_formacion = models.CharField(
        max_length=30,
        choices=constants.TIPO_FORMACION
    )
    estado = models.CharField(
        max_length=50,
        choices=constants.ESTADO_FORMACION
    )
    fecha_proceso = models.DateField(
        blank=True,
        null=True
    )
    observacion = models.TextField(
        blank=True,
        null=True
    )

