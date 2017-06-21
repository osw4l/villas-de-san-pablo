from django import forms
from . import models
from apps.utils import forms as utils, constants


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
    fecha_contratacion = forms.DateField(input_formats=constants.INPUT_FORMATS)

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.VacantePersona


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
