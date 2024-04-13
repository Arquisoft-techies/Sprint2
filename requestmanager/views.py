from django.http import HttpRequest, JsonResponse
from logic import request_logic

def crear_solicitud(request: HttpRequest):
    if request.method == 'POST':
        id = request.POST.get('id')
        tipo = request.POST.get('tipo')
        estado = request.POST.get('estado')
        respuesta = request_logic.crear_solicitud(id, tipo, estado)
        return JsonResponse({"mensaje": respuesta})

    else:
        return JsonResponse({'error': 'Tipo de solicitud no válido'}, status=400)

