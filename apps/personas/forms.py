from django import forms
from django.forms import models as models_form
from . import models
from apps.utils import forms as utils, constants


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
    fecha_ingreso = forms.DateField(input_formats=constants.INPUT_FORMATS)
    widget = forms.FileInput
    hoja_de_vida = forms.FileField(widget=widget)

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Persona


class ExperienciaLaboralForm(utils.BaseFormAllFields):
    title = 'Experiencia Laboral'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.ExperienciaLaboralPersona


def get_experiencia_laboral_persona_formset(form,
                                            formset=models_form.BaseInlineFormSet,
                                            **kwargs):
    return models_form.inlineformset_factory(
        models.Persona,
        models.ExperienciaLaboralPersona,
        form,
        formset,
        **kwargs
    )


class TipoFormacionComplementariaForm(utils.BaseFormAllFields):
    title = 'Tipo de formacion'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TipoFormacionComplementaria


class FormacionComplementariaForm(utils.BaseFormAllFields):
    title = 'Formacion Complementaria'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FormacionComplementariaPersona


def get_formacion_complementaria_persona_formset(form,
                                            formset=models_form.BaseInlineFormSet,
                                            **kwargs):
    return models_form.inlineformset_factory(
        models.Persona,
        models.FormacionComplementariaPersona,
        form,
        formset,
        **kwargs
    )