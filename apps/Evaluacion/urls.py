from django.urls import path
from apps.Evaluacion import views

app_name = 'eva'
urlpatterns = [
    path('verAreas/', views.verAreas, name="vArea"),
    path('crearArea/', views.crear_area, name="cArea"),
    path('modificarArea/<clave>', views.editarAreas, name="mArea"),
    path('verIndicadores/', views.verIndicadores, name="vindi"),
    path('crearIndicador/', views.crearIndicadores, name="cindi"),
    path('modificarIndicador/<clave>', views.editarIndicadores, name="mindi"),

]