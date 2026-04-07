from datetime import date

from django.http import JsonResponse
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def listar_tarefas_abertas(request):
    tarefas_abertas = Tarefa.objects.filter(status='ABERTA').values()
    return JsonResponse(list(tarefas_abertas), safe=False)

def listar_tarefas_prioridade(request, prioridade):
    tarefas_prioridade = Tarefa.objects.filter(prioridade=prioridade).values()
    return JsonResponse(list(tarefas_prioridade), safe=False)

def listar_tarefas_id(request, id):
    try:
        tarefa = Tarefa.objects.values().get(id=id)
        return JsonResponse(tarefa, safe=False)
    except Tarefa.DoesNotExist:
        return JsonResponse({'error': 'Tarefa não encontrada'}, status=404)

def listar_tarefas_abertas_prioridade_urgente(request):
    tarefas_abertas_urgentes = Tarefa.objects.filter(status='ABERTA', prioridade='URGENTE').values()
    return JsonResponse(list(tarefas_abertas_urgentes), safe=False)

def listar_tarefas_atrasadas(request):
    hoje = date.today()
    tarefas_atrasadas = Tarefa.objects.filter(data_entrega__lt=hoje).exclude(status='CONCLUIDA').values()
    return JsonResponse(list(tarefas_atrasadas), safe=False)

def listar_tarefas_buscar(request, termo):
    tarefas = Tarefa.objects.filter(titulo__icontains=termo).values()
    return JsonResponse(list(tarefas), safe=False)

