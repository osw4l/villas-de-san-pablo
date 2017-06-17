from django import forms
from . import models
from apps.utils import forms as utils


class VacanteForm(utils.BaseFormAllFields):
    title = 'Vacante'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Vacante

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields['fecha'])



class VacantePersonasForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.VacantePersona


class FormacionTrabajoForm(utils.BaseFormAllFields):
    title = 'Formacion para el trabajo'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FormacionTrabajo


class FormacionTrabajoPersonasForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FormacionTrabajoPersona
