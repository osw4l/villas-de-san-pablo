from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as auth_login
from apps.utils import views
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

@login_required
def salir(request):
    logout(request)
    return redirect('entrar')