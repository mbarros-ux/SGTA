from django.urls import path
from .views import (
    listar_tarefas,
    listar_tarefas_abertas,
    listar_tarefas_prioridade,
    listar_tarefas_id,
    listar_tarefas_abertas_prioridade_urgente,
    listar_tarefas_atrasadas,
    listar_tarefas_buscar,
)

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/abertas/', listar_tarefas_abertas),
    path('tarefas/prioridade/<str:prioridade>/', listar_tarefas_prioridade),
    path('tarefas/abertas/prioridade/urgente/', listar_tarefas_abertas_prioridade_urgente),
    path('tarefas/<int:id>/', listar_tarefas_id),
    path('tarefas/atrasadas/', listar_tarefas_atrasadas),
    path('tarefas/busca/<str:termo>/', listar_tarefas_buscar),
]