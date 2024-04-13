import random
from django.http import HttpRequest, JsonResponse
from .logic import send_request_to_login_handler, send_request_to_users_handler
from authenticator import crear_datos_iniciales, generar_datos_completos
from requestmanager import crear_solicitud
from usermanager import determinar_usuario_existe, almacenar_datos
from otp import generar_otp

def offers_view(request: HttpRequest):
    if request.method == 'POST':
        request_data = request.POST.get('datos')  # Obtener datos de la request

        basic_info = crear_datos_iniciales() # Metodo de manejador Login

        otp = generar_otp(6) # TODO: Metodo de generacion otp en app (api) otp

        crear_datos_iniciales(basic_info, otp) # Metodo de manejador login

        usuario_existe = determinar_usuario_existe(basic_info) # Metodo en manejador usuarios

        if usuario_existe == False:
            datos = generar_datos_completos(basic_info, False) # Generar datos aleatorios del usuario, metodo en login
            almacenar_datos(datos) # Metodo en manejador Usuarios
            print("El usuario fue creado exitosamente") # TODO: Mostrar en UI que se creo el usuario
        else:
            print("El usuario existe") # TODO: Qué más hacer si el usuario sí existe
        
        print(datos)

        random_id = random.randint(1, 100)
        request_tdc = HttpRequest()
        request_tdc.method = 'POST'
        request_tdc.POST['dato'] = 'valor'
        request_tdc.body = bytes(f'{{"id": {random_id}, "tipo": "Tarjeta basica", "estado": "En validacion"}}', encoding='utf-8')
        request_tdc.content_type = 'application/json'
        
        resultado_tdc = crear_solicitud(request_tdc) # Metodo de manejador Solicitudes
        print(resultado_tdc)

        '''# Determinar a qué manejador enviar la request
        request_type = determine_request_type(request_data)
        if request_type == 'login':
            response = send_request_to_login_handler(request_data)
        elif request_type == 'usuarios':
            response = send_request_to_users_handler(request_data)
        else:
            return JsonResponse({'error': 'type de request no válido'}, status=400)'''

        return JsonResponse({'error': 'Request finalizado'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def determine_request_type(request_data):
    if 'tipo' in request_data:
        type = request_data['tipo']
        return type
    return None