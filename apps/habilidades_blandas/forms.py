from django import forms
from django.forms import models as models_form
from apps.personas import models as persona_models
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


def get_habilidad_blanda_persona_formset(form,
                                         formset=models_form.BaseInlineFormSet,
                                         **kwargs):
    return models_form.inlineformset_factory(
        persona_models.Persona,
        models.HabilidadBlanda,
        form,
        formset,
        **kwargs
    )
