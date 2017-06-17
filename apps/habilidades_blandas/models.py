from django.db import models
from . import constants
# Create your models here.


class Capacitacion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Capacitaciones'
        verbose_name = 'Capacitacion'


class HabilidadBlanda(models.Model):
    persona = models.ForeignKey('personas.Persona')
    estado_certificado = models.CharField(
        max_length=30,
        choices=constants.ESTADO_CERTIFICADO
    )
    tipo_alerta = models.CharField(
        max_length=30,
        choices=constants.ALERTA,
        verbose_name='alertas'
    )
    test = models.BooleanField(
        default=False,
        verbose_name='Test de habilidades blandas'
    )
    observaciones = models.TextField(
        blank=True,
        null=True
    )

