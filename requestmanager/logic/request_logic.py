from .models import Solicitud

def crear_solicitud(tipo, estado):
    solicitud = Solicitud.objects.create(tipo=tipo, estado=estado)
    return solicitud