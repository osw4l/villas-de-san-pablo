from django import forms
from apps.utils import forms as utils
from . import models


class CapacitacionForm(utils.BaseFormAllFields):
    title = 'Capacitacion'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Capacitacion


class HabilidadBlandaForm(utils.BaseFormAllFields):
    title = 'Habilidad Blanda'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.HabilidadBlanda



