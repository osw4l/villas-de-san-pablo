from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^empleabilidad/', include('apps.api.empleabilidad.urls')),
    url(r'^emprendimiento/', include('apps.api.emprendimiento.urls')),
    url(r'^habilidades_blandas/', include('apps.api.habilidades_blandas.urls')),
    url(r'^personas/', include('apps.api.personas.urls')),
]
