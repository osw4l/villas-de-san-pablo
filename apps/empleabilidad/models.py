from django.db import models
from django.urls import reverse_lazy
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

    def get_update_url(self):
        return reverse_lazy('empleabilidad:editar_vacante',
                            kwargs={
                                'pk': self.pk
                            })


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

    def __str__(self):
        return '{} creado en {}'.format(
            self.nombre_programa,
            self.fecha_creacion
        )

    def get_update_url(self):
        return reverse_lazy('empleabilidad:editar_formacion_trabajo',
                            kwargs={
                                'pk': self.pk
                            })

    def personas(self):
        return FormacionTrabajoPersona.objects.filter(programa=self)


class FormacionTrabajoPersona(models.Model):
    programa = models.ForeignKey(FormacionTrabajo)
    persona = models.ForeignKey('personas.Persona')
    fecha_inscripcion = models.DateField()
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

