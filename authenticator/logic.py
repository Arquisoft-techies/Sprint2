from .models import Login
from .models import Signup
from .models import DatosInicial

def singup(existe, profesion, actividad, empresa, ingresos, deudas, idData):
    if(existe == True):
        #llamar a componente responsable para mostrar la info del usuario
        return ""
    else:
        actualizarDatos(profesion, actividad, empresa, ingresos, deudas, idData)

def createDatosInicial(nombres, apellidos, pais, ciudad, correo, numero, otp): #Añadir OTP
    variable = DatosInicial(nombres, apellidos, pais, ciudad, correo, numero, "", "", "", 0.0, 0.0, 0.0)
    variable.save()

def login(nombres, apellidos, pais, ciudad, correo, numero, otp):
    createDatosInicial(nombres, apellidos, pais, ciudad, correo, numero, otp) #Añadir OTP
    
def actualizarDatos(profesion, actividad, empresa, ingresos, deudas, idData):
    variable = DatosInicial.objects.get(id=idData)
    variable.profesion = profesion
    variable.actividadEconomica = actividad
    variable.empresa = empresa
    variable.ingresos = ingresos
    variable.deudas = deudas

def buscarPorOTP(numero):
    variable = DatosInicial.objects.get(otp = numero)
    return variable