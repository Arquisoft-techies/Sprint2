from django.http import HttpRequest, JsonResponse
from .logic import procesar_solicitud_login, procesar_solicitud_usuarios

def ofertas_view(request: HttpRequest):
    if request.method == 'POST':
        datos_solicitud = request.POST.get('datos')  # Obtener datos de la solicitud

        # Determinar a qué manejador enviar la solicitud
        tipo_solicitud = determinar_tipo_solicitud(datos_solicitud)
        if tipo_solicitud == 'login':
            respuesta = procesar_solicitud_login(datos_solicitud)
        elif tipo_solicitud == 'usuarios':
            respuesta = procesar_solicitud_usuarios(datos_solicitud)
        else:
            return JsonResponse({'error': 'Tipo de solicitud no válido'}, status=400)

        return JsonResponse(respuesta)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def determinar_tipo_solicitud(datos_solicitud):
    # Determinar si la solicitud se relaciona con productos o servicios
    if 'tipo' in datos_solicitud:
        tipo = datos_solicitud['tipo']
        if tipo == 'logs':
            return 'logs'
        elif tipo == 'analisisriesgos':
            return 'analisisriesgos'
        elif tipo == 'solicitudes':
            return 'solicitudes'
        elif tipo == 'documentos':
            return 'documentos'
    return None