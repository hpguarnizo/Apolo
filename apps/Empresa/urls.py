from django.urls import path
from apps.Empresa import views

app_name="empresa"
urlpatterns = [
    path('', views.index, name="index"),
    path('perfil/', views.perfil, name="perfil"),
    path('logout/', views.logout_view, name="logout"),
]
