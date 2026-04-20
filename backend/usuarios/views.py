from django.http import JsonResponse
from .models import Usuarios

def listar_usuarios(request):
    usuarios = Usuarios.objects.all().values()
    return JsonResponse(list(usuarios), safe=False)

def buscar_usuarios_por_id(request,id):
    try:
        usuarios = Usuarios.objects.values().get(id=id)
        return JsonResponse(usuarios, safe=False)
    except Usuarios.DoesNotExist:
        return JsonResponse({'error': 'Usuário não encontrado'}, status=404)

