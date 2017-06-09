from django.db import models

# Create your models here.


class Vacante(models.Model):
    cargo = models.CharField(max_length=30)
    salario = models.PositiveIntegerField()
    fecha = models.DateField()

    class Meta:
        verbose_name = 'Vacante'
        verbose_name_plural = 'Vacantes'

    def __str__(self):
        return '{} ${}'.format(self.cargo, self.salario)


class VacantePersona(models.Model):
    vacante = models.ForeignKey(Vacante)
    persona = models.ForeignKey('personas.Persona')
    

