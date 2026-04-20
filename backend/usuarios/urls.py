from django.urls import path
from .views import listar_usuarios, buscar_usuario

urlpatterns = [
    path('usuarios/', listar_usuarios),
    path('usuarios/id/<int:id>/', buscar_usuario)
]