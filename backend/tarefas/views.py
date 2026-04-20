from django.http import JsonResponse
from .models import Tarefa
from django.utils import timezone

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

def tarefas_urgente(request, prioridade):
    prioridade_upper = prioridade.upper()
    tarefas = Tarefa.objects.filter(prioridade=prioridade_upper).values()
    return JsonResponse(list(tarefas), safe=False)

def buscar_tarefa(request, id):
    try:
        tarefa = Tarefa.objects.get(pk=id)
        return JsonResponse({
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'status': tarefa.status,
            'prioridade': tarefa.prioridade,
            'data_entrega': str(tarefa.data_entrega),
        })
    
    except Tarefa.DoesNotExist:
        return JsonResponse('tarefa nao encontrada')
    
def tarefa_atrasada(request):
    hoje = timezone.now().date()
    tarefas = Tarefa.objects.filter(
        data_entrega=hoje).exclude(STATUS_CHOICES ='CONCLUIDA').values()
    return JsonResponse(list(tarefas), safe=False)

def tarefa_importante(request):
    tarefas = Tarefa.objects.filter(
        status='ABERTA', prioridade='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)
    
    
def tarefa_busca(request, titulo):
    tarefas = Tarefa.objects.filter(titulo__icontains=titulo).values()
    return JsonResponse(list(tarefas), safe=False)
