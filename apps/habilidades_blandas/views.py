from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from . import models
from . import forms
from apps.utils import views

class CapacitacionBaseView(object):
    model = models.Capacitacion
    form_class = forms.CapacitacionForm
    success_url = reverse_lazy('habilidades_blandas:lista_capacitacion')


class CapacitacionCreateView(CapacitacionBaseView, views.BaseCreateView):
    pass


class CapacitacionUpdateView(CapacitacionBaseView, views.BaseUpdateView):
    pass


class CapacitacionListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'Nombre')
    model = models.Capacitacion
    template_name = 'apps/habilidades_blandas/capacitacion_list.html'


class HabilidadesBlandasBaseView(object):
    model = models.HabilidadBlanda
    form_class = forms.HabilidadBlandaForm
    success_url = reverse_lazy('habilidades_blandas:lista_habilidades_blandas')


class HabilidadesBlandasCreateView(HabilidadesBlandasBaseView, views.BaseCreateView):
    pass


class HabilidadesBlandasUpdateView(HabilidadesBlandasBaseView, views.BaseUpdateView):
    pass


class HabilidadesBlandasListView(views.BaseListViewDinamicHeader):
    HEADER = ('Persona', 'Capacitacion', 'Estado Certificado', 'Tipo Alerta', 'Test', 'Observaciones')
    model = models.HabilidadBlanda
    template_name = 'apps/habilidades_blandas/habilidades_blandas_list.html'


