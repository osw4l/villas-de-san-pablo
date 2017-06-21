from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from apps.empleabilidad.forms import get_vacante_persona_formset as vacante_formset, \
    get_formacion_trabajo_persona_formset  as formacion_trabajo_formset
from apps.habilidades_blandas.forms import get_habilidad_blanda_persona_formset as habilidad_formset
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


@login_required
def crear_persona(request):
    form_class = forms.PersonaForm
    experienciaFormset = forms.get_experiencia_laboral_persona_formset(form_class, extra=1, can_delete=True)
    formacionFormset = forms.get_formacion_complementaria_persona_formset(form_class, extra=1, can_delete=True)
    vacanteFormset = vacante_formset(form_class, extra=1, can_delete=True)
    formacionTrabajoFormset = formacion_trabajo_formset(form_class, extra=1, can_delete=True)
    habilidadBlandaFormset = habilidad_formset(form_class, extra=1, can_delete=1)
    persona = models.Persona()
    form = forms.PersonaForm(request.POST or None, instance=persona)
    formset_1 = experienciaFormset(request.POST or None, instance=persona)
    formset_2 = formacionFormset(request.POST or None, instance=persona)
    formset_3 = vacanteFormset(request.POST or None, instance=persona)
    formset_4 = formacionTrabajoFormset(request.POST or None, instance=persona)
    formset_5 = habilidadBlandaFormset(request.POST or None, instance=persona)
    if request.POST:
        if form.is_valid() and formset_1.is_valid() and formset_2.is_valid()\
                and formset_3.is_valid() and formset_4.is_valid() and formset_5.is_valid():
            form.save()
            formset_1.save()
            formset_2.save()
            formset_3.save()
            formset_4.save()
            formset_5.save()
            return redirect('personas:lista_personas')

    context = {
        'form': form,
        'formset_1': formset_1,
        'formset_2': formset_2,
        'formset_3': formset_3,
        'formset_4': formset_4,
        'formset_5': formset_5,
        'action': 'Crear Persona'
    }
    return render(request, 'apps/personas/persona/base_form.html', context)


@login_required
def editar_persona(request, **kwargs):
    template_name = 'apps/personas/persona/base_form.html'
    form_class = forms.PersonaForm
    experienciaFormset = forms.get_experiencia_laboral_persona_formset(form_class, extra=0, can_delete=True)
    formacionFormset = forms.get_formacion_complementaria_persona_formset(form_class, extra=0, can_delete=True)
    pk = kwargs.get('pk')
    persona = models.Persona.objects.get(id=pk)
    form = forms.PersonaForm(request.POST or None, instance=persona)
    formset_1 = experienciaFormset(request.POST or None, instance=persona)
    formset_2 = formacionFormset(request.POST or None, instance=persona)
    if request.POST:
        if form.is_valid() and formset_1.is_valid() and formset_2.is_valid():
            form.save()
            formset_1.save()
            formset_2.save()
            return redirect('inventario:combos')

    context = {
        'form': form,
        'formset_1': formset_1,
        'formset_2': formset_2,
        'action': 'Crear Persona'
    }
    return render(request, template_name, context)


class TipoFormacionComplementariaBaseView(object):
    model = models.TipoFormacionComplementaria
    form_class = forms.TipoFormacionComplementariaForm
    success_url = reverse_lazy('personas:lista_tipos_formacion_complementaria')


class TipoFormacionComplementariaCreateView(TipoFormacionComplementariaBaseView,
                                          views.BaseCreateView):
    pass


class TipoFormacionComplementariaUpdateView(TipoFormacionComplementariaBaseView,
                                          views.BaseUpdateView):
    pass


class TipoFormacionComplementariaListView(views.BaseListViewDinamicHeader):
    HEADER = ('id', 'tipo de formacion complementaria')
    model = models.TipoFormacionComplementaria
    template_name = 'apps/personas/tipo_formacion_complementaria_list.html'