from django.shortcuts import render
from django.urls import reverse_lazy
from apps.utils import views
from . import models, forms
# Create your views here.


class TipoNegocioBaseView(object):
    model = models.TipoNegocio
    form_class = forms.TipoNegocioForm
    success_url = reverse_lazy('emprendimiento:lista_tipo_negocio')


class TipoNegocioCreateView(TipoNegocioBaseView, views.BaseCreateView):
    pass


class TipoNegocioUpdateView(TipoNegocioBaseView, views.BaseUpdateView):
    pass


class TipoNegocioListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'Nombre', 'Negocios')
    model = models.TipoNegocio
    template_name = 'apps/emprendimiento/tipo_negocio_list.html'


class TipoUnidadProductivaBaseView(object):
    model = models.TipoUnidadProductiva
    form_class = forms.TipoUnidadProductivaForm
    success_url = reverse_lazy('emprendimiento:lista_tipo_unidad_productiva')


class TipoUnidadProductivaCreateView(TipoUnidadProductivaBaseView, views.BaseCreateView):
    pass


class TipoUnidadProductivaUpdateView(TipoUnidadProductivaBaseView, views.BaseUpdateView):
    pass


class TipoUnidadProductivaListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'Nombre')
    model = models.TipoUnidadProductiva
    template_name = 'apps/emprendimiento/tipo_unidad_productiva_list.html'


class SectorBaseView(object):
    model = models.Sector
    form_class = forms.SectorForm
    success_url = reverse_lazy('emprendimiento:lista_sectores')


class SectorCreateView(SectorBaseView, views.BaseCreateView):
    pass


class SectorUpdateView(SectorBaseView, views.BaseUpdateView):
    pass


class SectorListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'Nombre')
    model = models.Sector
    template_name = 'apps/emprendimiento/sector_list.html'


class NegocioBaseView(object):
    model = models.Negocio
    form_class = forms.NegocioForm
    success_url = reverse_lazy('emprendiemiento:lista_negocio')


class NegocioCreateView(NegocioBaseView, views.BaseCreateView):
    pass


class NegocioUpdateView(NegocioBaseView, views.UpdateView):
    pass


class NegocioListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'Nombre', 'Direccion', 'Propietario', 'Tipo Negocio')
    model = models.Negocio
    template_name = 'apps/emprendimiento/negocio_list.html'


class EmpresasBaseView(object):
    model = models.Empresa
    form_class = forms.EmpresaForm
    success_url = reverse_lazy('emprendimiento:lista_empresa')


class EmpresaCreateView(EmpresasBaseView, views.BaseCreateView):
    pass


class EmpresaUpdateView(EmpresasBaseView, views.BaseUpdateView):
    pass


class EmpresaListView(EmpresasBaseView, views.BaseListViewDinamicHeader):
    HEADER = ('id', 'Nombre')
    model = models.Empresa
    template_name = 'apps/emprendimiento/empresa_list.html'


class EmprendimientoBaseView(object):
    model = models.Emprendimiento
    form_class = forms.EmprendimientoForm
    success_url = reverse_lazy('emprendimiento:lista_emprendimiento')


class EmprendimientoCreateView(EmprendimientoBaseView, views.BaseCreateView):
    pass


class EmprendimientoUpdateView(EmprendimientoBaseView, views.BaseUpdateView):
    pass


class EmprendimientoListView(EmprendimientoBaseView, views.BaseListViewDinamicHeader):
    HEADER = ('id', 'Persona', 'Tipo Negocio', 'Negocio', 'Ficha Caracterizacion', 'Ingreso Promedio Ventas', 'Ingreso Promedio Ventas Final', 'Tipo Unidad Productiva', 'Sector', 'Capital Semilla', 'Inscrito en:')
    model = models.Emprendimiento
    template_name = 'apps/emprendimiento/emprendimiento_list.html'


class OportunidadComercialBaseView(object):
    model = models.OportunidadComercial
    form_class = forms.OportunidadComercialForm
    sucess_url = reverse_lazy('emprendimiento:lista_oportunidad_comercial')


class OportunidadComercialCreateView(OportunidadComercialBaseView, views.BaseCreateView):
    pass


class OportuniadadComercialUpdateView(OportunidadComercialBaseView, views.BaseUpdateView):
    pass


class OportunidadComercialListView(OportunidadComercialBaseView, views.BaseListViewDinamicHeader):
    HEADER = ('id', 'Nombre', 'Negocio', 'Fecha', 'Empresa')
    model = models.OportunidadComercial
    template_name = 'apps/emprendimiento/oportunidad_comercial_list.html'


class FortalecimientoEmpresarialBaseView(object):
    model = models.FortalecimientoEmpresarial
    form_class = forms.FortalecimientoEmpresarialForm
    success_url = reverse_lazy('emprendimiento:lista_fortalecimiento_empresarial')


class FortalecimientoEmpresarialCreateView(FortalecimientoEmpresarialBaseView, views.BaseCreateView):
    pass


class FortalecimientoEmpresarialUpdateView(FortalecimientoEmpresarialBaseView, views.BaseUpdateView):
    pass


class FortalecimientoEmpresarialListView(FortalecimientoEmpresarialBaseView, views.BaseListViewDinamicHeader):
    HEADER = ('id', 'Personas', 'Tipo Negocio', 'Negocio', 'Emprendimiento', 'RUT', 'NIT', 'Camara de Comercio')
    model = models.FortalecimientoEmpresarial
    template_name = 'apps/emprendimiento/fortalecimiento_empresarial_list.html'










