from django.db import models
from . import constants
# Create your models here.


class Capacitacion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Capacitaciones'
        verbose_name = 'Capacitacion'

    def __str__(self):
        return self.nombre


class HabilidadBlanda(models.Model):
    persona = models.ForeignKey('personas.Persona', related_name='item_e')
    capacitacion = models.ForeignKey(Capacitacion, related_name='capacitacion_item')
    estado_certificado = models.CharField(
        max_length=30,
        choices=constants.ESTADO_CERTIFICADO,
        blank=True,
        null=True
    )
    tipo_alerta = models.CharField(
        max_length=30,
        choices=constants.ALERTA,
        verbose_name='alertas',
        blank=True,
        null=True
    )
    test = models.BooleanField(
        default=False,
        verbose_name='Test de habilidades blandas'
    )
    observaciones =models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

