from django.urls import path
from apps.Usuario import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name="index"),
    path('registro/', views.Registro_usuario, name="registro"),
    path('login/', views.login, name="login"),
]
