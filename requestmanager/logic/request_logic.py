from .models import Solicitud
import processing_logic
import register_logic

def crear_solicitud(id, tipo, estado):
    solicitud = Solicitud.objects.create(id=id, tipo=tipo, estado=estado)
    respuesta = procesamiento_solicitud(solicitud)
    return respuesta

def procesamiento_solicitud(solicitud): 
    procesamiento = processing_logic.crear_procesamiento(solicitud)
    informacion = register_logic.agregar_procesamiento_a_registro(procesamiento)
    informacion.save()
    return informacion
