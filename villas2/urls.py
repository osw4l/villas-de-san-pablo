"""villas2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from . import settings as base
from apps.main import views
from apps.utils import errors

urlpatterns = [
    url(r'^$', views.log_in, name='entrar'),
    url(r'^salir/', views.salir, name='salir'),
    url(r'^admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    # apps
    url(r'^empleabilidad/', include('apps.empleabilidad.urls', namespace='empleabilidad')),
    url(r'^emprendimiento/', include('apps.emprendimiento.urls', namespace='emprendimiento')),
    url(r'^habilidades_blandas/', include('apps.habilidades_blandas.urls', namespace='habilidades_blandas')),
    url(r'^main/', include('apps.main.urls', namespace='main')),
    url(r'^personas/', include('apps.personas.urls', namespace='personas')),

] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

handler400 = errors.error400
handler403 = errors.error403
handler404 = errors.error404
handler500 = errors.error500
