from ..models import Solicitud

def get_solicitudes():
    queryset = Solicitud.objects.all()
    return (queryset)

def get_solicitud(id):
    solicitud = Solicitud.objects.raw("SELECT * FROM Solicitudes_solicitud WHERE id=%s" % id)[0]
    return (solicitud)

def crear_solicitud(form):
    solicitud = form.save()
    solicitud.save()
    return ()

def aprobar_solicitud(solicitudId):
    try:
        solicitud = Solicitud.objects.get(Id=solicitudId)
        solicitud.status = True  
        solicitud.save()  
        return True  
    except Solicitud.DoesNotExist:
        return False  