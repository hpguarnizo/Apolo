from django.urls import path
from apps.Usuario import views


urlpatterns = [
    path('', views.index, name="index"),
    path('nuevo', views.Registro_usuario, name="crear"),
]
