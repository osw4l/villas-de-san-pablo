from django import forms
from . import models
from apps.utils import forms as utils


class GradoEscolaridadForm(utils.BaseFormAllFields):
    title = 'Grado de escolaridad'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.GradoEscolaridad


class TituloGradoForm(utils.BaseFormAllFields):
    title = 'Titulo de grado'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TituloGrado


class TipoViviendaForm(utils.BaseFormAllFields):
    title = 'Tipo de vivienda'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TipoVivienda


class TipoManzanaForm(utils.BaseFormAllFields):
    title = 'Tipo de manzana'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TipoManzana


class ManzanaForm(utils.BaseFormAllFields):
    title = 'Manzana'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Manzana


class CasaForm(utils.BaseFormAllFields):
    title = 'Casa'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Casa


class PersonaForm(utils.BaseFormAllFields):
    title = 'Persona'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Persona


class ExperienciaLaboralForm(utils.BaseFormAllFields):
    title = 'Experiencia Laboral'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.ExperienciaLaboralPersona


class TipoFormacionForm(utils.BaseFormAllFields):
    title = 'Tipo de formacion'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TipoFormacionComplementaria


class FormacionComplementariaForm(utils.BaseFormAllFields):
    title = 'Formacion Complementaria'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FormacionComplementariaPersona
