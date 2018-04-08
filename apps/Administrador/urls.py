from django.urls import path
from apps.Administrador import views

app_name = 'admon'
urlpatterns = [
    path('inicio/', views.index, name="inicio"),
    path('verEvaluacion/', views.verEvaluacion, name="verEva"),
    path('crearEvaluacion/', views.crearEvaluacion, name="crearEva"),
    path('verPlan/', views.verPlan, name="verPlan"),
    path('crearPlan/', views.crearPlan, name="crearPlan"),

]


