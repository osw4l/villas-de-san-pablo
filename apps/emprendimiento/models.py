from django.db import models
from django.urls import reverse_lazy
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.


class BaseUpdateUrl(object):
    attr_query = None

    def get_update_url(self):
        return reverse_lazy('emprendimiento:editar_{}'.format(self.attr_query), kwargs={'pk': self.pk})


class BaseName(models.Model, BaseUpdateUrl):
    nombre = models.CharField(max_length=150, unique=True)
    attr_query = None

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

    def get_attr_queryset_value(self):
        return {self.attr_query: self}

    def negocios(self):
        return Negocio.objects.filter(**self.get_attr_queryset_value())


class TipoNegocio(BaseName, BaseUpdateUrl):
    attr_query = 'tipo_negocio'

    class Meta:
        verbose_name = 'Tipo de negocio'
        verbose_name_plural = 'Tipos de negocio'


class TipoUnidadProductiva(BaseName, BaseUpdateUrl):
    attr_query = 'tipo_unidad_productiva'

    class Meta:
        verbose_name = 'Tipo de unidad productiva'
        verbose_name_plural = 'Tipos de unidades productivas'


class Sector(BaseName, BaseUpdateUrl):
    attr_query = 'sector'

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'


class Negocio(models.Model, BaseUpdateUrl):

    attr_query = 'negocio'

    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100)
    propietario = models.ForeignKey('personas.Persona')
    tipo_negocio = models.ForeignKey(TipoNegocio)

    class Meta:
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'

    def __str__(self):
        return '{} de {}, tipo de negocio : {}'.format(self.nombre, self.propietario, self.tipo_negocio)


class Empresa(BaseName, BaseUpdateUrl):
    attr_query = 'empresa'

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Emprendimiento(models.Model, BaseUpdateUrl):
    attr_query = 'emprendimiento'

    persona = models.ForeignKey('personas.Persona')
    tipo_negocio = models.ForeignKey(TipoNegocio)
    negocio = ChainedForeignKey(
        Negocio,
        chained_field='tipo_negocio',
        chained_model_field='tipo_negocio'
    )
    ficha_caracterizacion = models.BooleanField(default=False)
    ingreso_promedio_ventas = models.PositiveIntegerField(default=0)
    ingreso_promedio_ventas_finales = models.PositiveIntegerField(default=0)
    tipo_unidad_productova = models.ForeignKey(TipoUnidadProductiva)
    sector = models.ForeignKey(Sector)
    capital_semilla = models.PositiveIntegerField(default=0)
    inscrito_en = models.CharField(
        max_length=50,
        choices=(
            ('Fortalecimiento Empresarial', 'Fortalecimiento Empresarial'),
            ('Emprendimiento', 'Emprendimiento')
        )
    )

    class Meta:
        unique_together = ['persona', 'negocio']
        verbose_name = 'Emprendimiento'
        verbose_name_plural = 'Emprendimientos'

    def __str__(self):
        return 'emprendimiento #{},  {} a nombre de {}'.format(
            self.pk,
            self.negocio.nombre,
            self.negocio.propietario
        )


class OportunidadComercial(models.Model, BaseUpdateUrl):
    attr_query = 'oportunidad_comercial'

    negocio = models.ForeignKey(Emprendimiento)
    fecha = models.DateField()
    empresa = models.ForeignKey(Empresa)

    class Meta:
        verbose_name_plural = 'Oportunidades Comerciales'
        verbose_name = 'Oportunidad Comercial'


class FortalecimientoEmpresarial(models.Model, BaseUpdateUrl):
    attr_query = 'fortalecimiento_empresarial'

    persona = models.ForeignKey('personas.Persona')
    negocio = ChainedForeignKey(
        Negocio,
        chained_field='persona',
        chained_model_field='propietario'
    )
    emprendimiento = ChainedForeignKey(
        Emprendimiento,
        chained_field='negocio',
        chained_model_field='negocio'
    )
    rut = models.CharField(max_length=20, blank=True, null=True)
    nit = models.CharField(max_length=20, blank=True, null=True)
    camara_de_comercio = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Fortalecimiento Empresarial'
        verbose_name_plural = 'Fortalecimientos Empresariales'
