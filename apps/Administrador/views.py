from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request,"Administrador/index.html")

def verEvaluacion(request):
    return render(request,"Administrador/verEva.html")

def crearEvaluacion(request):
    return render(request,"Administrador/crearEva.html")

def verPlan(request):
    return render(request,"Administrador/verPlan.html")

def crearPlan(request):
    return render(request,"Administrador/crearPlan.html")