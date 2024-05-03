from django.http import HttpRequest, JsonResponse
from .logic import send_request_to_documents_handler, send_request_to_logs_handler, send_request_to_riskanalysis_handler, send_request_to_requests_handler

def offers_view(request: HttpRequest):
    if request.method == 'POST':
        request_data = request.POST.get('datos')  # Obtener datos de la request

        # Determinar a qué manejador enviar la request
        request_type = determine_request_type(request_data)

        """
        if request_type == 'logs':
            response = send_request_to_logs_handler(request_data)
        elif request_type == 'analisisriesgos':
            response = send_request_to_riskanalysis_handler(request_data)
        elif request_type == 'solicitudes':
            response = send_request_to_requests_handler(request_data)
        elif request_type == 'documentos':
            response = send_request_to_documents_handler(request_data)
        else:
            return JsonResponse({'error': 'type de request no válido'}, status=400)"""
        
        response = {
            'message': 'Solicitud recibida y procesada exitosamente'
        }

        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def determine_request_type(request_data):
    if 'tipo' in request_data:
        type = request_data['tipo']
        return type
    return None