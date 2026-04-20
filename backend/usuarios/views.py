from django.shortcuts import render
from django.http import JsonResponse
from .models import Usuario

# Create your views here.
def listar_usuarios(request):
    usuarios = Usuario.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

def buscar_usuario(request, id):
    try:
        usuario = Usuario.objects.get(pk=id)
        return JsonResponse({
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'ativo': usuario.ativo
        })
    except Usuario.DoesNotExist:
        return JsonResponse('Erro 404', 'Usuario não encontrado')