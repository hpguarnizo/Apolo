from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.Usuario.models import Persona
from apps.Usuario.forms import PersonaForm
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth import logout as dj_logout
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.

def login(request):
    if request.method == "POST":
        usuario = request.POST['correo']
        password = request.POST['pass']
        user = authenticate(username=usuario, password=password)
        persona = Persona.objects.get(username=request.POST["correo"])
        if user is not None:
            dj_login(request,user)
            return render(request, 'DashBoard/index.html', {'persona':persona})
        else:
            return render(request,"Home/login.html",{ 'Mensaje':'Los datos ingresados no son correctos.'})

    return render(request, 'Home/login.html',{ 'Mensaje':''})

def perfil(request):
    return render(request, 'Home/perfil.html')

def index(request):
    return render(request,"Home/index.html",{ 'Mensaje':'', 'señal':False})

def logout_view(request):
    dj_logout(request)
    return redirect('index')

def Registro_usuario(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if(form.is_valid()):
            formulario = form.save()
            #cifro contraseña
            formulario.set_password(form.cleaned_data['password'])
            formulario.save()
            #clono el correo en el campo user
            p = Persona.objects.get(username=request.POST["username"])
            p.email = request.POST["username"]
            p.save()
            return render(request, 'Home/registro.html', {'form':form, 'Mensaje':'se ha registrado el usuario con exito.','tipo':'success'})
        else:
            return render(request, 'Home/registro.html', {'form':form, 'Mensaje':'Se tiene un error en el formulario.','tipo':'danger'})
            
    else:
        form = PersonaForm()

    return render(request, 'Home/registro.html', {'form':form, 'Mensaje':'','tipo':'success'})