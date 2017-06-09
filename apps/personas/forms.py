from django import forms
from . import models
from apps.utils import forms as utils


class GradoEscolaridadForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.GradoEscolaridad


class TituloGradoForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TituloGrado


class TipoViviendaForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TipoVivienda


class TipoManzanaForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TipoManzana


class ManzanaForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Manzana


class CasaForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Casa


class PersonaForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Persona


class ExperienciaLaboralForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.ExperienciaLaboralPersona


class TipoFormacionForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TipoFormacionComplementaria


class FormacionComplementariaForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FormacionComplementariaPersona
