from otra_app_documentos.logic import procesar_solicitud_de_documentos

def enviar_solicitud_a_manejador_de_documentos(datos_solicitud):
    # TODO: Lógica para enviar la solicitud al manejador de documentos: llamar a la función correspondiente en la otra aplicación
    respuesta = procesar_solicitud_de_documentos(datos_solicitud)
    return respuesta