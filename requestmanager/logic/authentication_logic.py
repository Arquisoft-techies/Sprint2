from .models import AutenticacionSolicitud

def crear_autenticacion(solicitud, usuario, contrasena, estado_autenticacion, notas_autenticacion):
    autenticacion = AutenticacionSolicitud.objects.create(solicitud=solicitud, usuario=usuario,
                                                          contrasena=contrasena, estado_autenticacion=estado_autenticacion,
                                                          notas_autenticacion=notas_autenticacion)
    return autenticacion