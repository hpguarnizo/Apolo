from django.shortcuts import render
from apps.Usuario.models import Persona
from apps.Usuario.forms import PersonaForm
# Create your views here.

def index(request):
    if request.method == "POST":
        busqueda = list(Persona.objects.filter(username=request.POST["correo"]))
        if len(busqueda) > 0:
            persona = Persona.objects.get(username=request.POST["correo"])
            if(persona.password == request.POST["pass"]):
                return render(request, 'DashBoard/index.html', {'persona':persona})
            else:
                return render(request,"Home/index.html",{ 'Mensaje':'La contraseña es incorrecta.', 'señal':True})
        else:
            return render(request,"Home/index.html",{ 'Mensaje':'El correo electronico es incorrecto.', 'señal':True})

    return render(request,"Home/index.html",{ 'Mensaje':'', 'señal':False})

def Registro_usuario(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, 'index/registro.html', {'form':form, 'correto':'v'})
        elif request.POST["correo"] != '':
            persona = Persona.objects.get(username=request.POST["correo"])
            if(persona.password == request.POST["pass"]):
                return HttpResponse("Bienvenido al sistema " + persona.username)
            else:
                return HttpResponse("paso algo")

        return redirect('index')
    else:
        form = PersonaForm()

    return render(request, 'Home/registro.html', {'form':form, 'correto':'f'})