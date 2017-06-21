from django import forms
from . import models
from apps.utils import forms as utils, constants
from django.forms import models as models_form
from apps.personas import models as persona_models


class VacanteForm(utils.BaseFormAllFields):
    title = 'Vacante'
    fecha = forms.DateField(input_formats=constants.INPUT_FORMATS)

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Vacante

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data


class VacantePersonaForm(utils.BaseFormAllFields):
    title = 'Vacante Persona'
    fecha_contratacion = forms.DateField(
        input_formats=constants.INPUT_FORMATS,
        widget=forms.DateInput(attrs={'class': 'date'})
    )

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.VacantePersona


def get_vacante_persona_formset(form,
                                formset=models_form.BaseInlineFormSet,
                                **kwargs):
    return models_form.inlineformset_factory(
        persona_models.Persona,
        models.VacantePersona,
        form,
        formset,
        **kwargs
    )


class FormacionTrabajoForm(utils.BaseFormAllFields):
    title = 'Formacion para el trabajo'
    fecha_creacion = forms.DateField(input_formats=constants.INPUT_FORMATS)

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FormacionTrabajo


class FormacionTrabajoPersonasForm(utils.BaseFormAllFields):
    title = 'Formacion Trabajo Persona'
    fecha_inscripcion = forms.DateField(input_formats=constants.INPUT_FORMATS)
    fecha_proceso = forms.DateField(input_formats=constants.INPUT_FORMATS)

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FormacionTrabajoPersona


def get_formacion_trabajo_persona_formset(form,
                                          formset=models_form.BaseInlineFormSet,
                                          **kwargs):
    return models_form.inlineformset_factory(
        persona_models.Persona,
        models.FormacionTrabajoPersona,
        form,
        formset,
        **kwargs
    )