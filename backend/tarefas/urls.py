from django.urls import path
from .views import listar_tarefas, tarefas_urgente, buscar_tarefa, tarefa_atrasada, tarefa_importante, tarefa_busca

urlpatterns = [
    path('tarefas/', listar_tarefas),
    path('tarefas/prioridade/<str:prioridade>/', tarefas_urgente),
    path('tarefas/id/<int:id>/', buscar_tarefa),
    path('tarefas/atrasadas', tarefa_atrasada),
    path('tarefas/importante', tarefa_importante),
    path('tarefas/busca/<str:titulo>/', tarefa_busca)
]