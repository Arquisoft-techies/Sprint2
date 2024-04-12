from otra_app_solicitudes.logic import procesar_solicitud_de_solicitudes

def enviar_solicitud_a_manejador_de_solicitudes(datos_solicitud):
    # TODO: Lógica para enviar la solicitud al manejador de solicitudes: llamar a la función correspondiente en la otra aplicación
    respuesta = procesar_solicitud_de_solicitudes(datos_solicitud)
    return respuesta