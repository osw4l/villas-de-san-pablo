from django import forms
from apps.utils import forms as utils, constants
from . import models


class TipoNegocioForm(utils.BaseFormAllFields):
    title = 'Tipo Negocio'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TipoNegocio


class TipoUnidadProductivaForm(utils.BaseFormAllFields):
    title = 'Tipo Unidad Productiva'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.TipoUnidadProductiva


class SectorForm(utils.BaseFormAllFields):
    title = 'Sector'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Sector


class NegocioForm(utils.BaseFormAllFields):
    title = 'Negocio'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Negocio


class EmpresaForm(utils.BaseFormAllFields):
    title = 'Empresa'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Empresa


class EmprendimientoForm(utils.BaseFormAllFields):
    title = 'Emprendimiento'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.Emprendimiento


class OportunidadComercialForm(utils.BaseFormAllFields):
    title = 'Oportunidad Comercial'
    fecha = forms.DateField(input_formats=constants.INPUT_FORMATS)

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.OportunidadComercial


class FortalecimientoEmpresarialForm(utils.BaseFormAllFields):
    title = 'Fortalecimiento Empresarial'

    class Meta(utils.BaseFormAllFields.Meta):
        model = models.FortalecimientoEmpresarial

