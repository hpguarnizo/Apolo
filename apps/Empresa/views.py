from django.shortcuts import render
from apps.Empresa.models import Empresa
from apps.Usuario.models import Persona
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    if request.method == "POST":
        persona = Persona.objects.get(email=request.POST["correo"])
        if(persona.password == request.POST["pass"]):
            return render(request, 'DashBoard/index.html', {'persona':persona})
        else:
            return HttpResponse("paso algo")

    return render(request,"index/index.html")