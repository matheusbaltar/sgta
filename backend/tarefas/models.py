from django.db import models
from usuarios.models import Usuario

STATUS_CHOICES = [
    ('ABERTA', 'Aberta'),
    ('EM_ANDAMENTO', 'Em andamento'),
    ('CONCLUIDA', 'Concluida'),
    ('CANCELADA', 'Cancelada'),
]

STATUS_PRIORIDADE = [
    ('NAO_URGENTE', 'Nao urgente'),
    ('URGENTE', 'Urgente')
]

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aberta')
    usuario_responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()
    prioridade = models.CharField(max_length=20, choices=STATUS_PRIORIDADE, default='NAO_URGENTE')


    def __str__(self):
        return self.titulo
    
    