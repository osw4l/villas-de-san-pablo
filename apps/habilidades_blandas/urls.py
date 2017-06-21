from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^crear-capacitacion/',
        views.CapacitacionCreateView.as_view(),
        name='crear_capacitacion'),

    url(r'^editar-capacitacion/',
        views.CapacitacionUpdateView.as_view(),
        name='editar_capacitacion'),

    url(r'^lista-capacitacion/',
        views.CapacitacionListView.as_view(),
        name='lista_capacitacion'),

    url(r'^crear-habilidades-blandas/',
        views.HabilidadesBlandasCreateView.as_view(),
        name='crear_habilidades_blandas'),

    url(r'^editar-habilidades-blandas/',
        views.HabilidadesBlandasUpdateView.as_view(),
        name='editar_habilidades_blandas'),

    url(r'^list-habilidades-blandas',
        views.HabilidadesBlandasListView.as_view(),
        name='lista_habilidades_blandas'),

]
