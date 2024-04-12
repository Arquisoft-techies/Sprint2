# TODO: Arreglar import
from otra_app_login.logic import procesar_solicitud_de_login

def enviar_solicitud_a_manejador_de_login(datos_solicitud):
    # TODO: Lógica para enviar la solicitud al manejador de login: llamar a la función correspondiente en la otra aplicación
    respuesta = procesar_solicitud_de_login(datos_solicitud)
    return respuesta