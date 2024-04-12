from .models import ProcesamientoSolicitud

def crear_procesamiento(autenticacion, aprobacion, notas_procesamiento, respuesta_texto):
    procesamiento = ProcesamientoSolicitud.objects.create(autenticacion=autenticacion, aprobacion=aprobacion,
                                                          notas_procesamiento=notas_procesamiento,
                                                          respuesta_texto=respuesta_texto)
    return procesamiento