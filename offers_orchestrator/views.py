from django.http import HttpRequest, JsonResponse
from .logic import procesar_solicitud_producto, procesar_solicitud_servicio

def ofertas_view(request: HttpRequest):
    if request.method == 'POST':
        datos_solicitud = request.POST.get('datos')  # Obtener datos de la solicitud

        # Determinar a qué manejador enviar la solicitud
        tipo_solicitud = determinar_tipo_solicitud(datos_solicitud)
        if tipo_solicitud == 'producto':
            respuesta = procesar_solicitud_producto(datos_solicitud)
        elif tipo_solicitud == 'servicio':
            respuesta = procesar_solicitud_servicio(datos_solicitud)
        else:
            return JsonResponse({'error': 'Tipo de solicitud no válido'}, status=400)

        return JsonResponse(respuesta)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def determinar_tipo_solicitud(datos_solicitud):
    # Determinar si la solicitud se relaciona con productos o servicios
    if 'tipo' in datos_solicitud:
        tipo = datos_solicitud['tipo']
        if tipo == 'producto':
            return 'producto'
        elif tipo == 'servicio':
            return 'servicio'
    return None