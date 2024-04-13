import random
import string
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
from sprint.authenticator.logic import login
from sprint.authenticator.logic import signup
from sprint.authenticator.logic import buscarPorOTP
from django.http import JsonResponse
from .forms import LoginForm
from .forms import SingupForm
from django.core.serializers import serialize

# Create your views here.
#def recibirRequest(request):


def crearDatosInciales():
    #parsed_data = json.loads(basic_info)
    nombres = ["Sara", "Tomás", "Matías", "Alejandra", "Ignacio", "Gabriela"]
    lastNames = ["Celis Rengifo", "Bacca Sanchez", "Álvarez Sosa", "Soler Galvis", "Sandoval Moreno"]
    ciudades = ["Bogota", "Cali", "Medellín", "Cartagena", "Barranquilla"]
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domains = ["gmail.com", "outlook.com", "yahoo.com"]
    domain = random.choice(domains)
    email = f"{local_part}@{domain}"
    area_code = random.randint(300, 360)
    prefix = random.randint(000, 999)
    line_number = random.randint(0000, 9999)
    phone_number = f"({area_code}) {prefix} {line_number}"
    name = random.choice(nombres)
    apellidos = random.choice(lastNames)
    pais = "Colombia"
    ciudad = random.choice(ciudades)
    correo = email
    numero = phone_number
    datos = login(name, apellidos, pais, ciudad, correo, numero)
    serializada = serialize('json', datos)
    return JsonResponse(serializada, safe=False)

# def obtenerOTP(request):
    #if request.method == "POST":
        #numero = request.data['otp']
        #info = buscarPorOTP(numero)
        #data = { "id": info.id}
        #return JsonResponse(data) 

def generar_datos_completos(basic_info, existe):
            if existe == False:
                    parsed_data = json.loads(basic_info)
                    profesiones = ["Doctor", "Ingeniero", "Literato", "Físico", "Profesor"]
                    actividades = ["Eduación", "Consultoría", "Entretenimiento", "Asalariado"]
                    empresas =  ["UniAlpes", "Google", "Random house of Penguins", "CERN"]
                    parsed_data = json.loads(basic_info)
                    numero = parsed_data["numero"]
                    existe = False
                    profesion = random.choice(profesiones)
                    actividad = random.choice(actividades)
                    empresa = random.choice(empresas)
                    ingresos = random.randint(1, 100)
                    deudas = random.randint(1, 100)
                    informacionCompleta = signup(existe, profesion, actividad, empresa, ingresos, deudas, numero)
                    serializada = serialize('json', informacionCompleta)
                    return JsonResponse(serializada, safe=False)
