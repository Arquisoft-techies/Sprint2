import random
from .models import ProcesamientoSolicitud

def crear_procesamiento(solicitud):
    aprobacion = random.choice([True, False])

    if aprobacion:
        notas_procesamiento = "Buen perfil financiero, responsable con sus gastos y pagos."
    else:
        notas_procesamiento = "Perfil poco confiable, grandes indices de riesgos."

    procesamiento = ProcesamientoSolicitud.objects.create(solicitud=solicitud, aprobacion=aprobacion,
                                                          notas_procesamiento=notas_procesamiento)
    return procesamiento