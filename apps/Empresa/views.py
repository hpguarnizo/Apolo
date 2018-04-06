from django.http import HttpResponse
from django.shortcuts import render,redirect
from apps.Empresa.models import Empresa
from apps.Usuario.models import Persona
from apps.Evaluacion.models import Resultados_Evaluacion
from apps.Empresa.forms import Registro_empresa_Form
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='usuarios:login')
def index(request):
    username = request.session['pk_user']
    persona = Persona.objects.get(username=username)
    persona_empresa = list(Empresa.objects.filter(usuario=persona))
    if len(persona_empresa) > 0:
        empresa = Empresa.objects.get(usuario=persona)
        return render(request,"DashBoard/index.html",{'empresa':empresa})
    else:
        return redirect('empresa:registro')

@login_required(login_url='usuarios:login')
def logout_view(request):
    #try:
    #    del request.session['pk_user']
    #except KeyError:
    #    pass
    #causa un error cuando se hace el llamado 
    django_logout(request)
    return redirect('user:index')

@login_required(login_url='usuarios:login')
def perfil(request):
    if 'pk_user' in request.session:
        username = request.session['pk_user']
        persona = Persona.objects.get(username=username)
        empresa = Empresa.objects.get(usuario=persona)
        Numero_evaluciones_R = list(Resultados_Evaluacion.objects.filter(Empresas=empresa))
        return render(request, 'Home/perfil.html',{'empresa':empresa,'Contador':len(Numero_evaluciones_R)})
    else:
        django_logout(request)
        return redirect('user:index')

@login_required(login_url='usuarios:login')
def registro_empresa(request):

    #Busco el contexto de persona
    username = request.session['pk_user']
    persona = Persona.objects.get(username=username)

    if request.method == 'POST':
        formulario_empresa = Registro_empresa_Form(request.POST)
        if(formulario_empresa.is_valid()):
            #Guardo formulario de registro de usuario
            formulario = formulario_empresa.save(commit=False)

            minimo_vigente = 781242
            if int(formulario.Numero_empleados) < 10 or int(formulario.Activos) < 500*minimo_vigente:
                formulario.Tipo_empresa = "Micro"
            elif int(formulario.Numero_empleados) > 10 or int(formulario.Numero_empleados) < 50 or int(formulario.Activos) > 501*minimo_vigente or int(formulario.Activos) < 5000*minimo_vigente:
                formulario.Tipo_empresa = "Pequeña"
            else:
                formulario.Tipo_empresa = "Mediana"    
            formulario.usuario = persona
            formulario.save()
            
            return redirect('empresa:index')
        else:
            return render(request, 'Empresa/registro_empresa.html', {'form':formulario_empresa, 'Mensaje':'Se tiene un error en el formulario.','tipo':'danger','empresa':'','persona':persona})
            
    else:
        formulario_empresa = Registro_empresa_Form()

    return render(request, 'Empresa/registro_empresa.html', {'form':formulario_empresa, 'Mensaje':'','tipo':'success','empresa':'','persona':persona})