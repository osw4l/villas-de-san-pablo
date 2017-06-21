from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^crear-sector/',
        views.SectorCreateView.as_view(),
        name='crear_sector'),

    url(r'^editar-sector/(?P<pk>\d+)/',
        views.SectorUpdateView.as_view(),
        name='editar_sector'),

    url(r'^lista-sectores/',
        views.SectorListView.as_view(),
        name='lista_sectores'),



]
