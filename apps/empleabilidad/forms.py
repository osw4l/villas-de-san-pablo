from django import forms
from . import models
from apps.utils import forms as utils


class VacanteForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Vacante


class VacantePersonasForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.VacantePersona


class FormacionTrabajoForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FormacionTrabajo


class FormacionTrabajoPersonasForm(utils.BaseFormAllFields):
    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FormacionTrabajoPersona
