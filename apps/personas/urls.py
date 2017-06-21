from django.conf.urls import url
from . import views

urlpatterns = [

   # tipos de formacion complementaria

    url(r'^crear-tipo-formacion-complementaria/',
        views.TipoFormacionComplementariaCreateView.as_view(),
        name='crear_tipo_formacion_complementaria'),

    url(r'^editar-tipo-formacion-complementaria/(?P<pk>\d+)/',
        views.TipoFormacionComplementariaUpdateView.as_view(),
        name='editar_tipo_formacion_complementaria'),

    url(r'^lista-tipos-formacion-complementaria/',
        views.TipoFormacionComplementariaListView.as_view(),
        name='lista_tipos_formacion_complementaria'),

    # grados de escolaridad

    url(r'^crear-grado-escolaridad/',
        views.GradoEscolaridadCreateView.as_view(),
        name='crear_grado_escolaridad'),

    url(r'^editar-grado-escolaridad/(?P<pk>\d+)/',
        views.GradoEscolaridadUpdateView.as_view(),
        name='editar_grado_escolaridad'
        ),

    url(r'^lista-grados-escolaridad/',
        views.GradoEscolaridadListView.as_view(),
        name='lista_grados_escolaridad'),

    # titulos de grado

    url(r'^crear-titulo-grado/',
        views.TituloGradoCreateView.as_view(),
        name='crear_titulo_grado'),

    url(r'^editar-titulo-grado/(?P<pk>\d+)/',
        views.TituloGradoUpdateView.as_view(),
        name='editar_titulo_grado'),

    url(r'^lista-titulos-grado/',
        views.TituloGradoListView.as_view(),
        name='lista_titulos_grado'),

    # tipos de manzana

    url(r'^crear-tipo-manzana/',
        views.TipoManzanaCreateView.as_view(),
        name='crear_tipo_manzana'),

    url(r'^editar-tipo-manzana/(?P<pk>\d+)/',
        views.TipoManzanaUpdateView.as_view(),
        name='editar_tipo_manzana'),

    url(r'^lista-tipos-manzana/',
        views.TipoManzanaListView.as_view(),
        name='lista_tipos_manzana'),

    # tipos de vivienda

    url(r'^crear-tipo-vivienda/',
        views.TipoViviendaCreateView.as_view(),
        name='crear_tipo_vivienda'),

    url(r'^editar-tipo-vivienda/(?P<pk>\d+)/',
        views.TipoViviendaUpdateView.as_view(),
        name='editar_tipo_vivienda'),

    url(r'^lista-tipos-vivienda/',
        views.TipoViviendaListView.as_view(),
        name='lista_tipos_vivienda'),

    # manzanas

    url(r'^crear-manzana/',
        views.ManzanaCreateView.as_view(),
        name='crear_manzana'),

    url(r'^editar-manzana/(?P<pk>\d+)/',
        views.ManzanaUpdateView.as_view(),
        name='editar_manzana'),

    url(r'^lista-manzanas/',
        views.ManzanaListView.as_view(),
        name='lista_manzanas'),

    # casas

    url(r'^crear-casa/',
        views.CasaCreateView.as_view(),
        name='crear_casa'),

    url(r'^editar-casa/(?P<pk>\d+)/',
            views.CasaUpdateView.as_view(),
        name='editar_casa'),

    url(r'^lista-casas/',
        views.CasaListView.as_view(),
        name='lista_casas'),

    # personas

    url(r'^crear-persona/',
        views.crear_persona,
        name='crear_persona'),

    url(r'^editar-persona/',
        views.crear_persona,
        name='editar_persona'),

    url(r'^lista-persona/',
        views.PersonasListView.as_view(),
        name='lista_persona')


]
