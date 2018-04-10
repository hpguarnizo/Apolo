from django.shortcuts import render,redirect
from django.urls import reverse
from apps.Usuario.models import Persona
from apps.Administrador.models import Administrador
from apps.Usuario.forms import Registro_Persona_Form
from apps.Administrador.forms import Registro_Administrador_Form
from apps.Evaluacion.forms import Registro_area
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.decorators import login_required
from apps.Evaluacion.models import Area


def login(request):
    if request.method == "POST":
        usuario = request.POST['correo']
        password = request.POST['pass']
        busqueda = list(Persona.objects.filter(username=usuario))
        if len(busqueda) > 0:
            user = authenticate(username=usuario, password=password)
            persona = Persona.objects.get(username=request.POST["correo"])
            if user is not None:
                dj_login(request,user)
                request.session['pk_admon'] = persona.username
                return redirect('admon:inicio')
            else:
                return render(request,"Home/login.html",{ 'Mensaje':'La contraseña es incorrecta.'})
        else:
            return render(request,"Home/login.html",{ 'Mensaje':'El correo electronico ingresado no es valido'})

    return render(request, 'Home/login.html',{ 'Mensaje':''})

@login_required(login_url='admon:registro')
def index(request):
    username = request.session['pk_admon']
    persona = Persona.objects.get(username=username)
    admin = Administrador.objects.get(usuario=persona)
    
    return render(request,"Administrador/index.html",{'admin':admin})
    

def verEvaluacion(request):
    return render(request,"Administrador/verEva.html")


def crearEvaluacion(request):
    return render(request,"Administrador/crearEva.html")

def verPlan(request):
    return render(request,"Administrador/verPlan.html")

def crearPlan(request):
    return render(request,"Administrador/crearPlan.html")

def Registro_administrador(request):
    if request.method == 'POST':
        formulario_persona = Registro_Persona_Form(request.POST)
        formulario_admin = Registro_Administrador_Form(request.POST);
        if(formulario_persona.is_valid() & formulario_admin.is_valid()):
            if request.POST["password"] == request.POST["c_contraseña"]:
                #Guardo formulario de registro de usuario
                formulario = formulario_persona.save(commit=False)
                formulario_admin_s = formulario_admin.save(commit=False)
            
                #cifro contraseña
                formulario.set_password(formulario_persona.cleaned_data['password'])
                formulario.email = request.POST["username"]
                formulario.save()

                formulario_admin_s.usuario = formulario
                formulario_admin_s.save()
                return render(request, 'Administrador/registro_admin.html', {'form':formulario_persona, 'form_admin': formulario_admin,'Mensaje':'se ha registrado el usuario con exito.','tipo':'success'})
            else:
                return render(request, 'Administrador/registro_admin.html', {'form':formulario_persona, 'form_admin': formulario_admin, 'Mensaje':'Las contraseñas no coinciden.','tipo':'danger'})
        else:
            return render(request, 'Administrador/registro_admin.html', {'form':formulario_persona, 'form_admin': formulario_admin, 'Mensaje':'Se tiene un error en el formulario.','tipo':'danger'})
            
    else:
        formulario_persona = Registro_Persona_Form()
        formulario_admin = Registro_Administrador_Form()

    return render(request, 'Administrador/registro_admin.html', {'form':formulario_persona,'form_admin': formulario_admin, 'Mensaje':'','tipo':'success'})

@login_required(login_url='admon:registro')
def logout_view(request):
    #try:
    #    del request.session['pk_user']
    #except KeyError:
    #    pass
    #causa un error cuando se hace el llamado 
    django_logout(request)
    return redirect('admon:login')