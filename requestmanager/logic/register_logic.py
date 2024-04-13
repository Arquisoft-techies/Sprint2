from .models import RegistroSolicitud

def agregar_procesamiento_a_registro(procesamiento):
    registro = RegistroSolicitud.objects.create()
    registro.procesamiento_solicitud.add(procesamiento)
    respuesta = f"{procesamiento.aprobacion}-{procesamiento.notas_procesamiento}"
    return respuesta