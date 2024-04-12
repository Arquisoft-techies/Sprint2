from django.http import HttpRequest, JsonResponse
from logic import solicitud_logic, autenticacion_logic, procesamiento_logic, registro_logic

def procesar_solicitud(autenticacion, aprobacion, notas_procesamiento, respuesta_texto):
    procesamiento = procesamiento_logic.crear_procesamiento(autenticacion, aprobacion,
                                                            notas_procesamiento, respuesta_texto)
    return procesamiento

def registrar_solicitud(procesamiento):
    registro = registro_logic.agregar_procesamiento_a_registro(procesamiento)
    return registro

def crear_solicitud(request: HttpRequest):
    if request.method == 'POST':
        id = request.POST.get('id')
        tipo = request.POST.get('tipo')
        estado = request.POST.get('estado')

        solicitud = solicitud_logic.crear_solicitud(id, tipo, estado)
        return HttpRequest("Solicitud creada exitosamente!")
    else:
        return  HttpRequest({'error': 'Tipo de solicitud no válido'}, status=400)

def autenticar_solicitud(request: HttpRequest):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')

        autenticacion = autenticacion_logic.autenticar_solicitud(usuario, contrasena)

        if autenticacion:
            return HttpRequest("Solicitud autenticada exitosamente!")
        else:
            return HttpRequest({'error': 'Autenticacion fallida'}, status=401)
    else:
        return  JsonResponse({'error': 'Tipo de solicitud no válido'}, status=400)