from .models import Login
from .models import Signup
from .models import DatosInicial

def signup(existe, profesion, actividad, empresa, ingresos, deudas, idData):
    if(existe == True):
        #llamar a componente responsable para mostrar la info del usuario
        return ""
    else:
        actualizarDatos(profesion, actividad, empresa, ingresos, deudas, idData)

def createDatosInicial(nombres, apellidos, pais, ciudad, correo, numero, otp): 
    datos = DatosInicial(nombres, apellidos, pais, ciudad, correo, numero, "", "", "", 0.0, 0.0, otp)
    datos.save()

def login(nombres, apellidos, pais, ciudad, correo, numero, otp):
    createDatosInicial(nombres, apellidos, pais, ciudad, correo, numero, otp) 
    
def actualizarDatos(profesion, actividad, empresa, ingresos, deudas, idData):
    datos = DatosInicial.objects.get(id=idData)
    datos.profesion = profesion
    datos.actividadEconomica = actividad
    datos.empresa = empresa
    datos.ingresos = ingresos
    datos.deudas = deudas
    datos.save()

def buscarPorOTP(numero):
    variable = DatosInicial.objects.get(otp = numero)
    return variable