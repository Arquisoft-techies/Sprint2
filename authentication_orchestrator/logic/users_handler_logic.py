from otra_app_usuarios.logic import procesar_solicitud_de_usuarios

def enviar_solicitud_a_manejador_de_usuarios(datos_solicitud):
    # TODO: Lógica para enviar la solicitud al manejador de usuarios: llamar a la función correspondiente en la otra aplicación
    respuesta = procesar_solicitud_de_usuarios(datos_solicitud)
    return respuesta