from django.db import models

# Create your models here.
STATUS_USUARIO = [
    ('ATIVO', 'ativo'),
    ('INATIVO', 'inativo')
]
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    ativo = models.CharField(max_length=10, choices=STATUS_USUARIO, default='ativo')
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome