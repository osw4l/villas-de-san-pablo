from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^inicio/',
        views.InicioTemplateView.as_view(),
        name='inicio'),

]
