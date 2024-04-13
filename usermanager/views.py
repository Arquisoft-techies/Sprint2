from django.http import HttpRequest, JsonResponse
from logic import *
from .logic import consultar_datos_logic, buscar_informacion_cliente

def determinar_usuario_existe(basic_info):
    cliente_existe = consultar_datos_logic.usuario_existe(basic_info)
    if cliente_existe:
        datos_cliente = consultar_datos_logic.obtener_informacion_cliente(basic_info)
        return datos_cliente

    else:
        return None

def consultar_usuario(basic_info):
    if request.method == 'GET':
        numero_identificacion = request.GET.get('numero_identificacion')
        datos_cliente = buscar_informacion_cliente(numero_identificacion)

        if datos_cliente: 
            return JsonResponse({'cliente': datos_cliente})
        else:
            return JsonResponse({'error': 'Cliente no encontrado'}, status=404)
        
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def actualizar_cliente(request: HttpRequest):
    if request.method == 'POST':
        numero_identificacion = request.POST.get('numero_identificacion')

        nuevos_datos = {
            'nombre': request.POST.get('nombre'),
            'apellidos': request.POST.get('apellidos')
        }

        actualizacion_exitosa = actualizar_datos_cliente(numero_identificacion, nuevos_datos)

        if actualizacion_exitosa:
            return JsonResponse({'mensaje': 'Los datos del cliente se actualizaron correctamente'})
        else:
            return JsonResponse({'error': 'Cliente no encontrado'}, status=404)

    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

