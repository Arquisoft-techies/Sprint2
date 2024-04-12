from django.http import HttpRequest, JsonResponse
from .logic import send_request_to_login_handler, send_request_to_users_handler

def offers_view(request: HttpRequest):
    if request.method == 'POST':
        request_data = request.POST.get('datos')  # Obtener datos de la request

        # Determinar a qué manejador enviar la request
        request_type = determine_request_type(request_data)
        if request_type == 'login':
            response = send_request_to_login_handler(request_data)
        elif request_type == 'usuarios':
            response = send_request_to_users_handler(request_data)
        else:
            return JsonResponse({'error': 'type de request no válido'}, status=400)

        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def determine_request_type(request_data):
    if 'tipo' in request_data:
        type = request_data['tipo']
        return type
    return None