import random
from django.http import HttpRequest, JsonResponse
from .logic import send_request_to_login_handler, send_request_to_users_handler

def offers_view(request: HttpRequest):
    if request.method == 'POST':
        request_data = request.POST.get('datos')  # Obtener datos de la request

        # TODO: Recibir datos básicos que el usuario llena

        basic_info = convertir_datos_JSON # Metodo de manejador Login

        otp = generar_otp # TODO: Metodo de generacion otp en app otp

        crear_datos_iniciales(basic_info, otp) # Metodo de manejador login

        usuario_existe = determinar_usuario_existe(basic_info) # TODO: Metodo en manejador usuarios

        if usuario_existe == False:
            datos = generar_info(basic_info) # Generar datos aleatorios del usuario
            almacenar_datos(datos) # TODO: Metodo en manejador Usuarios
            # Mostrar en UI que se creo el usuario
        else:
            print(datos)

        random_id = random.randint(1, 100)
        request_tdc = HttpRequest()
        request_tdc.method = 'POST'
        request_tdc.POST['dato'] = 'valor'
        request_tdc.body = bytes(f'{{"id": {random_id}, "tipo": "Tarjeta basica", "estado": "En validacion"}}', encoding='utf-8')
        request_tdc.content_type = 'application/json'

        
        resultado_tdc = crear_solicitud(request_tdc) # TODO: Metodo de manejador Login






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