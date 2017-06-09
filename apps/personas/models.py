from django.db import models
from . import constants
from django.core import validators
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.


class GradoEscolaridad(models.Model):
    nombre_grado_escolaridad = models.CharField(
        max_length=30,
        unique=True
    )

    class Meta:
        verbose_name = 'Grado de escolaridad'
        verbose_name_plural = 'Grados de escolaridad'

    def __str__(self):
        return '{}'.format(self.nombre_grado_escolaridad)

    def personas(self):
        return Persona.objects.filter(grado_escolaridad=self)


class TituloGrado(models.Model):
    nombre_titulo = models.CharField(
        max_length=50,
        unique=True
    )
    grado_escolaridad = models.ForeignKey(GradoEscolaridad)

    class Meta:
        verbose_name = 'Titulo Grado'
        verbose_name_plural = 'Titulo Grados'

    def __str__(self):
        return '{}'.format(self.grado_escolaridad)

    def personas(self):
        return Persona.objects.filter(titulo_grado=self)


class TipoVivienda(models.Model):
    nombre_tipo_vivienda = models.CharField(
        max_length=30,
        unique=True
    )

    class Meta:
        verbose_name = 'Tipo de Vivienda'
        verbose_name_plural = 'Tipos de Vivienda'

    def __str__(self):
        return '{}'.format(self.nombre_tipo_vivienda)

    def personas(self):
        return Persona.objects.filter(tipo_vivienda=self)


class TipoManzana(models.Model):
    nombre_tipo_manzana = models.CharField(
        max_length=30,
        unique=True
    )

    class Meta:
        verbose_name = 'Tipo de Manzana'
        verbose_name_plural = 'Tipos de Manzana'

    def __str__(self):
        return '{}'.format(self.nombre_tipo_manzana)

    def personas(self):
        return Persona.objects.filter(tipo_manzana=self)


class Manzana(models.Model):
    numero_manzana = models.SmallIntegerField()
    tipo_manzana = models.ForeignKey(TipoManzana)

    class Meta:
        verbose_name = 'Manzana'
        verbose_name_plural = 'Manzanas'
        unique_together = ['numero_manzana', 'tipo_manzana']

    def __str__(self):
        return 'Manzana #{}'.format(self.numero_manzana)

    def personas(self):
        return Persona.objects.filter(manzana=self)


class Casa(models.Model):
    direccion_casa = models.CharField(
        max_length=30,
        unique=True
    )
    numero_casa = models.SmallIntegerField()
    numero_telefono = models.CharField(max_length=15)
    numero_telefono_2 = models.CharField(max_length=15)
    numero_telefono_3 = models.CharField(max_length=15)
    numero_manzana = models.ForeignKey(Manzana)
    tipo_vivienda = models.ForeignKey(TipoVivienda)

    class Meta:
        verbose_name = 'Manzana'
        verbose_name_plural = 'Manzanas'

    def __str__(self):
        return 'casa {} manzana {} - {}'.format(
            self.numero_casa,
            self.numero_manzana,
            self.direccion_casa
        )

    def personas(self):
        return Persona.objects.filter(casa=self)


class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(
        max_length=12,
        choices=constants.SEXO
    )
    estado_civil = models.CharField(
        max_length=20,
        choices=constants.ESTADO_CIVIL
    )
    edad = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(100)
        ]
    )
    telefono_1 = models.CharField(max_length=12, blank=True, null=True)
    telefono_2 = models.CharField(max_length=12, blank=True, null=True)
    telefono_3 = models.CharField(max_length=12, blank=True, null=True)
    fecha_de_registro = models.DateField(auto_now_add=True)
    fecha_ingreso = models.DateField()
    tiene_empleo = models.BooleanField(default=False)
    origen_ingreso = models.CharField(max_length=50)
    ingreso_promedio_mensual = models.PositiveIntegerField(blank=True, null=True)
    ingreso_promedio_familiares = models.PositiveIntegerField(blank=True, null=True)
    ingreso_promedio_mensuales = models.PositiveIntegerField(blank=True, null=True)
    vulnerabilidad = models.BooleanField(default=False)

    hoja_de_vida = models.FileField(upload_to='cv', blank=True, null=True)
    cv_last_update = models.DateField(blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    # educacion
    grado_escolaridad = models.ForeignKey(GradoEscolaridad)
    titulo_grado = ChainedForeignKey(
        TituloGrado,
        chained_field='grado_escolaridad',
        chained_model_field='grado_escolaridad'
    )

    tipo_vivienda = models.ForeignKey(TipoVivienda)
    tipo_manzana = models.ForeignKey(TipoManzana)
    manzana = ChainedForeignKey(
        Manzana,
        chained_field='tipo_manzana',
        chained_model_field='tipo_manzana'
    )
    casa = ChainedForeignKey(
        Casa,
        chained_field='manzana',
        chained_model_field='manzana'
    )


class ExperienciaLaboralPersona(models.Model):
    persona = models.ForeignKey(Persona)
    nombre = models.CharField(
        max_length=255,
        verbose_name='Experiencia laboral'
    )
    lapso_de_tiempo = models.CharField(
        max_length=20,
        choices=constants.LAPSOS
    )
    cantidad_de_tiempo = models.PositiveIntegerField()


class TipoFormacionComplementaria(models.Model):
    nombre = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Nombre del tipo de formacion complementaria'
    )

    class Meta:
        verbose_name = 'Tipo de formacion complementaria'
        verbose_name_plural = 'Tipos de formacion complementaria'

    def __str__(self):
        return self.nombre


class FormacionComplementariaPersona(models.Model):
    persona = models.ForeignKey(Persona)
    nombre_curso = models.CharField(max_length=30)
    tipo_formacion = models.ForeignKey(TipoFormacionComplementaria)


