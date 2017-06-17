from django.conf.urls import url
from . import views

urlpatterns = [

    # vacantes

    url(r'^crear-vacante/',
        views.VacanteCreateView.as_view(),
        name='crear_vacante'),

    url(r'^editar-vacante/(?P<pk>\d+)/',
        views.VacanteUpdateView.as_view(),
        name='editar_vacante'),

    url(r'^lista-vacantes/',
        views.VacanteListView.as_view(),
        name='lista_vacantes'),

    # formacion para el trabajo

    url(r'^crear-formacion-trabajo/',
        views.FormacionTrabajoCreateView.as_view(),
        name='crear_formacion_trabajo'),

    url(r'^editar-formacion-trabajo/(?P<pk>\d+)/',
        views.FormacionTrabajoUpdateView.as_view(),
        name='editar_formacion_trabajo'),

    url(r'^lista-formaciones-trabajo/',
        views.FormacionTrabajoListView.as_view(),
        name='lista_formaciones_trabajo')


]
