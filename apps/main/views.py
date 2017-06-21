from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as auth_login
from apps.utils import views
from apps.personas.models import Casa, Manzana, Persona
from apps.empleabilidad.models import Vacante
from apps.emprendimiento.models import Negocio, Emprendimiento, Empresa, OportunidadComercial
# Create your views here.


def log_in(request):
    context = {'error': False}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('main:inicio')
            else:
                context = {'msj': 'El usuario ha sido desactivado', 'error': True}
        else:
            context = {'msj': 'usuario o contraseña incorrecta', 'error': True}
    return render(request, 'login.html', context)


class InicioTemplateView(views.BaseTemplateView):
    template_name = 'apps/main/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['casas'] = Casa.objects.all().count()
        context['personas'] = Persona.objects.all().count()
        context['manzanas'] = Manzana.objects.all().count()
        context['vacantes'] = Vacante.objects.all().count()
        # otro bloque
        context['negocios'] = Negocio.objects.all().count()
        context['emprendimientos'] = Emprendimiento.objects.all().count()
        context['empresas'] = Empresa.objects.all().count()
        context['oportunidades_comerciales'] = OportunidadComercial.objects.all().count()
        return context

@login_required
def salir(request):
    logout(request)
    return redirect('entrar')
