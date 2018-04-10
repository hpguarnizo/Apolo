from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Evaluacion.models import Area
from apps.Evaluacion.models import Indicador
from apps.Evaluacion.forms import Registro_area, Registro_indicador
from apps.Usuario.models import Persona
from apps.Administrador.models import Administrador

# Create your views here.
@login_required(login_url='administrador:login')
def verAreas(request):
    areas = Area.objects.all()
    username = request.session['pk_admon']
    persona = Persona.objects.get(username=username)
    admin = Administrador.objects.get(usuario=persona)
    return render(request,"Administrador/verArea.html",{'admin':admin,'areas':areas})

@login_required(login_url='administrador:login')
def verIndicadores(request):
    indicadores = Indicador.objects.all()
    username = request.session['pk_admon']
    persona = Persona.objects.get(username=username)
    admin = Administrador.objects.get(usuario=persona)
    return render(request,"Administrador/verIndicador.html",{'admin':admin,'indicadores':indicadores})

@login_required(login_url='administrador:login')
def crear_area(request):
    username = request.session['pk_admon']
    persona = Persona.objects.get(username=username)
    admin = Administrador.objects.get(usuario=persona)
    if request.method == 'POST':
        formulario_area = Registro_area(request.POST)
        if(formulario_area.is_valid()):
            formulario_area.save()

            return render(request,"Administrador/crearArea.html",{'admin':admin, 'form_area': formulario_area,'Mensaje':'Se ha creado el área con éxito','tipo':'success', 'icono':'check'})
        else:
            return render(request,"Administrador/crearArea.html",{'admin':admin, 'form_area': formulario_area,'Mensaje':'Ha ocurrido un error','tipo':'danger','icono':'close-circle-o'})
    else:
       formulario_area = Registro_area()
            
    return render(request,"Administrador/crearArea.html",{'admin':admin, 'form_area': formulario_area,'Mensaje':'','tipo':'','icono':''})

@login_required(login_url='administrador:login')
def crearIndicadores(request):
    username = request.session['pk_admon']
    persona = Persona.objects.get(username=username)
    admin = Administrador.objects.get(usuario=persona)
    if request.method == 'POST':
        formulario_indicador = Registro_indicador(request.POST)
        if(formulario_indicador.is_valid()):
            formulario_indicador.save()

            return render(request,"Administrador/crearIndicador.html",{'admin':admin, 'form_area': formulario_indicador,'Mensaje':'Se ha creado el área con éxito','tipo':'success', 'icono':'check'})
        else:
            return render(request,"Administrador/crearIndicador.html",{'admin':admin, 'form_area': formulario_indicador,'Mensaje':'Ha ocurrido un error','tipo':'danger','icono':'close-circle-o'})
    else:
       formulario_indicador = Registro_indicador()
            
    return render(request,"Administrador/crearIndicador.html",{'admin':admin, 'form_area': formulario_indicador,'Mensaje':'','tipo':'','icono':''})

def editarAreas(request,clave):
    username = request.session['pk_admon']
    persona = Persona.objects.get(username=username)
    admin = Administrador.objects.get(usuario=persona)
    area = Area.objects.get(pk=clave)
    if request.method == 'GET':
        form = Registro_area(instance=area)
    else:
        form = Registro_area(request.POST,instance=area)
        if form.is_valid():
            form.save()
            return redirect('eva:vArea')
        else:
            return HttpResponse()
            
    return render(request,"Administrador/editarIndicador.html",{'admin':admin, 'form_area': form,'Mensaje':'','tipo':'','icono':''})

def editarIndicadores(request,clave):
    username = request.session['pk_admon']
    persona = Persona.objects.get(username=username)
    admin = Administrador.objects.get(usuario=persona)
    indi = Indicador.objects.get(pk=clave)
    if request.method == 'GET':
        form = Registro_indicador(instance=indi)
    else:
        form = Registro_indicador(request.POST,instance=indi)
        if form.is_valid():
            form.save()
            return redirect('eva:vindi')
        else:
            return HttpResponse()
    return render(request,"Administrador/editarIndicador.html",{'admin':admin, 'form_area': form,'Mensaje':'','tipo':'','icono':''})
