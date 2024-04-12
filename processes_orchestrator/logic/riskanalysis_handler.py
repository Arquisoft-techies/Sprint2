# TODO: Arreglar import
from otra_app_analisisriesgos.logic import procesar_solicitud_de_analisisriesgos

def enviar_solicitud_a_manejador_de_analisisriesgos(datos_solicitud):
    # TODO: Lógica para enviar la solicitud al manejador de analisisriesgos: llamar a la función correspondiente en la otra aplicación
    respuesta = procesar_solicitud_de_analisisriesgos(datos_solicitud)
    return respuesta