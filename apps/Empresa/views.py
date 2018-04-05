from django.http import HttpResponse
from django.shortcuts import render,redirect
from apps.Empresa.models import Empresa
from apps.Usuario.models import Persona
from apps.Empresa.forms import Registro_empresa_Form
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    username = request.session['pk_user']
    persona = Persona.objects.get(username=username)
    persona_empresa = list(Empresa.objects.filter(usuario=persona))
    if len(persona_empresa) > 0:
        empresa = Empresa.objects.get(usuario=persona)
        return render(request,"DashBoard/index.html",{'persona':persona,'empresa':empresa})
    else:
        return redirect('empresa:registro')

@login_required
def logout_view(request):
    #try:
    #    del request.session['pk_user']
    #except KeyError:
    #    pass
    #causa un error cuando se hace el llamado 
    #django_logout(request)
    return redirect('user:index')

@login_required
def perfil(request):
    return render(request, 'Home/perfil.html')

@login_required
def registro_empresa(request):

    #Busco el contexto de persona
    username = request.session['pk_user']
    persona = Persona.objects.get(username=username)

    if request.method == 'POST':
        formulario_empresa = Registro_empresa_Form(request.POST)
        if(formulario_empresa.is_valid()):
            
            #Guardo formulario de registro de usuario
            formulario = formulario_empresa.save()

            #clono el correo en el campo user
            e = Empresa.objects.get(NIT=request.POST["NIT"])
            e.usuario = persona
            e.save()
            
            return redirect('empresa:index')
        else:
            return render(request, 'Home/registro.html', {'form':formulario_empresa, 'Mensaje':'Se tiene un error en el formulario.','tipo':'danger'})
            
    else:
        formulario_empresa = Registro_empresa_Form()

    return render(request, 'Home/registro.html', {'form':formulario_empresa, 'Mensaje':'','tipo':'success'})