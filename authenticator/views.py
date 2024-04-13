import random
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

# Create your views here.
#def recibirRequest(request):


def crearDatosInciales(basic_info, otp):
    parsed_data = json.loads(basic_info)
    name = parsed_data["nombres"]
    apellidos = parsed_data["apellidos"]
    pais = parsed_data["pais"]
    ciudad = parsed_data["ciudad"]
    correo = parsed_data["correo"]
    numero = parsed_data["numero"]
    data = {
                "datos recibidos"
    }
    login(name, apellidos, pais, ciudad, correo, numero, otp)
    return JsonResponse(data)

def obtenerOTP(request):
    if request.method == "POST":
        numero = request.data['otp']
        info = buscarPorOTP(numero)
        data = { "id": info.id}
        return JsonResponse(data)

def actualizarDatosInciales(request):
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            existe = False
            profesion = form["profesion"].value()
            actividad = form["actividad"].value()
            empresa = form["empresa"].value()
            ingresos = form["ingresos"].value()
            deudas = form["deudas"].value()
            idData = request.data['id']
            signup(existe, profesion, actividad, empresa, ingresos, deudas, idData)
            messages.add_message(request, messages.SUCCESS, "Creado exitosamente")
            respuesta = {"respuesta": "creado exitosamente"}
            return JsonResponse(respuesta)
        else:
            print(form.errors)