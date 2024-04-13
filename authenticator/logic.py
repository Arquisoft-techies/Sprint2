from .models import Login
from .models import Signup
from .models import DatosInicial

def signup(existe, profesion, actividad, empresa, ingresos, deudas, number):
    if(existe == True):
        #llamar a componente responsable para mostrar la info del usuario
        return ""
    else:
        return actualizarDatos(profesion, actividad, empresa, ingresos, deudas, number)

def createDatosInicial(nombres, apellidos, pais, ciudad, correo, numero, otp): 
    datos = DatosInicial(nombres, apellidos, pais, ciudad, correo, numero, "", "", "", 0.0, 0.0, otp)
    datos.save()

def login(nombres, apellidos, pais, ciudad, correo, numero, otp):
    createDatosInicial(nombres, apellidos, pais, ciudad, correo, numero, otp) 
    
def actualizarDatos(profesion, actividad, empresa, ingresos, deudas, number):
    datos = DatosInicial.objects.get(numero=number)
    datos.profesion = profesion
    datos.actividadEconomica = actividad
    datos.empresa = empresa
    datos.ingresos = ingresos
    datos.deudas = deudas
    datos.save()
    return datos

def buscarPorOTP(numero):
    variable = DatosInicial.objects.get(otp = numero)
    return variable