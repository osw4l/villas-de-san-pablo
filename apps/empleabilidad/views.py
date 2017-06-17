from django.shortcuts import render
from django.urls import reverse_lazy

from apps.utils import views
from . import models, forms
# Create your views here.


class VacanteBaseView(object):
    model = models.Vacante
    form_class = forms.VacanteForm
    success_url = reverse_lazy('empleabilidad:lista_vacantes')


class VacanteCreateView(VacanteBaseView, views.BaseCreateView):
    pass


class VacanteUpdateView(VacanteBaseView, views.BaseUpdateView):
    pass


class VacanteListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'cargo', 'salario', 'fecha')
    model = models.Vacante
    template_name = 'apps/empleabilidad/vacante_list.html'


class FormacionTrabajoBaseView(object):
    model = models.FormacionTrabajo
    form_class = forms.FormacionTrabajoForm
    success_url = reverse_lazy('empleabilidad:lista_formaciones_trabajo')


class FormacionTrabajoCreateView(FormacionTrabajoBaseView, views.BaseCreateView):
    pass


class FormacionTrabajoUpdateView(FormacionTrabajoBaseView, views.BaseUpdateView):
    pass


class FormacionTrabajoListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'fecha de creacion', 'nombre del programa')
    model = models.FormacionTrabajo
    template_name = 'apps/empleabilidad/formacion_trabajo_list.html'

