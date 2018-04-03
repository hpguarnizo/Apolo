from django.shortcuts import render,redirect
from apps.Empresa.models import Empresa
from apps.Usuario.models import Persona
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    username = request.session['pk_user']
    persona = Persona.objects.get(username=username)
    return render(request,"DashBoard/index.html",{'persona':persona})

@login_required
def logout_view(request):
    try:
        del request.session['pk_user']
    except KeyError:
        pass
    #causa un error cuando se hace el llamado 
    #django_logout(request)
    return redirect('user:index')

@login_required
def perfil(request):
    return render(request, 'Home/perfil.html')