from django.shortcuts import render
from django.urls import reverse_lazy
from apps.utils import views
from . import models, forms
# Create your views here.


class TipoNegocioBaseView(object):
    model = models.TipoNegocio
    form_class = forms.TipoNegocioForm
    success_url = reverse_lazy('emprendimiento:lista_tipos_negocio')


class TipoNegocioCreateView(TipoNegocioBaseView, views.BaseCreateView):
    pass


class TipoNegocioUpdateView(TipoNegocioBaseView, views.BaseUpdateView):
    pass


class TipoNegocioListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'nombre', 'negocios')
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
    HEADER = ('id', 'nombre', 'negocios')
    model = models.TipoUnidadProductiva
    template_name = 'apps/emprendimiento/tipo_negocio_list.html'


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

