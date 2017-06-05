from django.db import models

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


class Manzana(models.Model):
    numero_manzana = models.SmallIntegerField()
    tipo_manzana = models.ForeignKey(TipoManzana)

    class Meta:
        verbose_name = 'Manzana'
        verbose_name_plural = 'Manzanas'
        unique_together = ['numero_manzana', 'tipo_manzana']

    def __str__(self):
        return '{}'.format(self.numero_manzana)


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


class Personas(models.Model):
    nombre_personas = models.CharField(max_length=30)
    apellido_personas = models.CharField(max_length=30)
    sexo_personas = models.CharField(max_length=12)
    edad_personas = models.CharField(max_length=2)
    fecha_ingreso = models.DateField()
    empleo = models.BooleanField(default=False)
    origen_ingreso = models.CharField(max_length=10)
    ingreso_promedio_mensual = models.CharField(max_length=10)
    hoja_de_vida = models.FileField(upload_to='cv')
    email = models.EmailField()













