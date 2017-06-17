from django.shortcuts import render
from django.urls import reverse_lazy

from apps.utils import views
from . import models
from . import forms
# Create your views here.


class GradoEscolaridadBaseView(object):
    model = models.GradoEscolaridad
    success_url = reverse_lazy('personas:lista_grados_escolaridad')
    form_class = forms.GradoEscolaridadForm


class GradoEscolaridadCreateView(GradoEscolaridadBaseView, views.BaseCreateView):
    pass


class GradoEscolaridadUpdateView(GradoEscolaridadBaseView, views.BaseUpdateView):
    pass


class GradoEscolaridadListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'nombre grado', 'personas')
    model = models.GradoEscolaridad
    template_name = 'apps/personas/grado_escolaridad_list.html'


class TituloGradoBaseView(object):
    model = models.TituloGrado
    success_url = reverse_lazy('personas:lista_titulos_grado')
    form_class = forms.TituloGradoForm


class TituloGradoCreateView(TituloGradoBaseView, views.BaseCreateView):
    pass


class TituloGradoUpdateView(TituloGradoBaseView, views.BaseUpdateView):
    pass


class TituloGradoListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'nombre titulo', 'grado de escolaridad', 'personas')
    model = models.TituloGrado
    template_name = 'apps/personas/titulo_grado_list.html'


class TipoManzanaBaseView(object):
    model = models.TipoManzana
    success_url = reverse_lazy('personas:lista_tipos_manzana')
    form_class = forms.TipoManzanaForm


class TipoManzanaCreateView(TipoManzanaBaseView, views.BaseCreateView):
    pass


class TipoManzanaUpdateView(TipoManzanaBaseView, views.BaseUpdateView):
    pass


class TipoManzanaListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'nombre', 'personas', 'casas')
    model = models.TipoManzana
    template_name = 'apps/personas/tipo_manzana_list.html'


class TipoViviendaBaseView(object):
    model = models.TipoVivienda
    form_class = forms.TipoViviendaForm
    success_url = reverse_lazy('personas:lista_tipos_vivienda')


class TipoViviendaCreateView(TipoViviendaBaseView, views.BaseCreateView):
    pass


class TipoViviendaUpdateView(TipoViviendaBaseView, views.BaseUpdateView):
    pass


class TipoViviendaListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'nombre', 'personas', 'casas')
    model = models.TipoVivienda
    template_name = 'apps/personas/tipo_vivienda_list.html'


class ManzanaBaseView(object):
    model = models.Manzana
    form_class = forms.ManzanaForm
    success_url = reverse_lazy('personas:lista_manzanas')


class ManzanaCreateView(ManzanaBaseView, views.BaseCreateView):
    pass


class ManzanaUpdateView(ManzanaBaseView, views.BaseUpdateView):
    pass


class ManzanaListView(views.BaseListViewDinamicHeader):
    HEADER = ('numero', 'tipo', 'personas', 'casas')
    model = models.Manzana
    template_name = 'apps/personas/manzana_list.html'


class CasaBaseView(object):
    model = models.Casa
    form_class = forms.CasaForm
    success_url = reverse_lazy('personas:lista_casas')


class CasaCreateView(CasaBaseView, views.BaseCreateView):
    pass


class CasaUpdateView(CasaBaseView, views.BaseUpdateView):
    pass


class CasaListView(views.BaseListViewDinamicHeader):
    HEADER = ('# casa', 'direccion', 'tipo de manzana',
              '# manzana', 'tipo de vivienda', 'telefonos', 'personas')
    model = models.Casa
    template_name = 'apps/personas/casa_list.html'

