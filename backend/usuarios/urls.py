from django.urls import path
from .views import listar_usuarios, buscar_usuarios_por_id

urlpatterns = [
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/<int:id>/', buscar_usuarios_por_id, name='buscar_usuarios_por_id'),
]