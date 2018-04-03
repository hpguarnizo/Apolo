from django.urls import path
from apps.Usuario import views


urlpatterns = [
    path('', views.index, name="index"),
    path('registro/', views.Registro_usuario, name="crear"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('perfil/', views.perfil, name="perfil"),
]
