from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^crear-tipo-negocio/',
        views.TipoNegocioCreateView.as_view(),
        name='crear_tipo_negocio'),

    url(r'^editar-tipo-negocio/(?P<pk>\d+)/',
        views.TipoNegocioUpdateView.as_view(),
        name='editar_tipo_negocio'),

    url(r'^lista-tipo-negocio/',
        views.TipoNegocioListView.as_view(),
        name='lista_tipo_negocio'),

    url(r'^crear-tipo-unidad-productiva/',
        views.TipoUnidadProductivaCreateView.as_view(),
        name='crear_tipo_unidad_productiva'),

    url(r'^editar-tipo-unidad-productiva/(?P<pk>\d+)',
        views.TipoUnidadProductivaUpdateView.as_view(),
        name='editar_tipo_unidad_productiva'),

    url(r'^lista-tipo-unidad-productiva/',
        views.TipoUnidadProductivaListView.as_view(),
        name='lista_tipo_unidad_productiva'),

    url(r'^crear-sector/',
        views.SectorCreateView.as_view(),
        name='crear_sector'),

    url(r'^editar-sector/(?P<pk>\d+)/',
        views.SectorUpdateView.as_view(),
        name='editar_sector'),

    url(r'^lista-sectores/',
        views.SectorListView.as_view(),
        name='lista_sectores'),

    url(r'^crear-negocios/',
        views.NegocioCreateView.as_view(),
        name='crear_negocio'),

    url(r'^editar-negocio/(?P<pk>\d+)',
        views.NegocioUpdateView.as_view(),
        name='editar_negocio'),

    url(r'^lista-negocio/',
        views.NegocioListView.as_view(),
        name='lista_negocio'),

    url(r'^crear-empresa/',
        views.EmpresaCreateView.as_view(),
        name='crear_empresa'),

    url(r'^editar-empresa/(?P<pk>\d+)',
        views.EmpresaUpdateView.as_view(),
        name='editar_empresa'),

    url(r'^lista-empresa/',
        views.EmpresaListView.as_view(),
        name='lista_empresa'),

    url(r'^crear-emprendimiento/',
        views.EmprendimientoCreateView.as_view(),
        name='crear_emprendimiento'),

    url(r'^editar-empresa/(?P<pk>\d+)',
        views.EmpresaUpdateView.as_view(),
        name='editar_empresa'),

    url(r'^lista-emprendimiento/',
        views.EmprendimientoListView.as_view(),
        name='lista_emprendimiento'),

    url(r'^crear-oportunidad-comercial/',
        views.OportunidadComercialCreateView.as_view(),
        name='crear_oportunidad_comercial'),

    url(r'^editar-oportunidad-comercial/(?P<pk>\d+)',
        views.OportuniadadComercialUpdateView.as_view(),
        name='editar_emprendimiento'),

    url(r'^lista-oportunidad-comercial/',
        views.OportunidadComercialListView.as_view(),
        name='lista_oportunidad_comercial'),

    url(r'^crear-fortalecimiento-empresarial/',
        views.FortalecimientoEmpresarialCreateView.as_view(),
        name='crear_fortalecimiento_empresarial'),

    url(r'^editar_fortalecimiento_empresarial/(?P<pk>\d+)',
        views.FortalecimientoEmpresarialUpdateView.as_view(),
        name='editar_fortalecimiento_empresarial'),

    url(r'^lista-fortalecimiento-empresarial/',
        views.FortalecimientoEmpresarialListView.as_view(),
        name='lista_fortalecimiento_empresarial'),
]

