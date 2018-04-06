from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from apps.Usuario.models import Persona
from apps.Usuario.forms import Registro_Persona_Form
from django.contrib.auth import authenticate, login as dj_login
from django.conf import settings
from django.urls import reverse
from apps.Empresa.views import index
from django.conf import settings
# Create your views here.

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
                request.session['pk_user'] = persona.username
                return redirect('empresas:index')
            else:
                return render(request,"Home/login.html",{ 'Mensaje':'La contraseña es incorrecta.'})
        else:
            return render(request,"Home/login.html",{ 'Mensaje':'El correo electronico ingresado no es valido'})

    return render(request, 'Home/login.html',{ 'Mensaje':''})

def index(request):
    if not request.user.is_authenticated:
        return render(request,"Home/index.html")
    else:
        return redirect('empresas:index')


def Registro_usuario(request):
    if request.method == 'POST':
        formulario_persona = Registro_Persona_Form(request.POST)
        if(formulario_persona.is_valid()):
            if request.POST["password"] == request.POST["c_contraseña"]:
                #Guardo formulario de registro de usuario
                formulario = formulario_persona.save(commit=False)

                #cifro contraseña
                formulario.set_password(formulario_persona.cleaned_data['password'])
                formulario.email = request.POST["username"]
                formulario.save()
                return render(request, 'Home/registro.html', {'form':formulario_persona, 'Mensaje':'se ha registrado el usuario con exito.','tipo':'success'})
            else:
                return render(request, 'Home/registro.html', {'form':formulario_persona, 'Mensaje':'Las contraseñas no coinciden.','tipo':'danger'})
        else:
            return render(request, 'Home/registro.html', {'form':formulario_persona, 'Mensaje':'Se tiene un error en el formulario.','tipo':'danger'})
            
    else:
        formulario_persona = Registro_Persona_Form()

    return render(request, 'Home/registro.html', {'form':formulario_persona, 'Mensaje':'','tipo':'success'})