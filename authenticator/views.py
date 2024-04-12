import random
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from sprint.authenticator.logic import login
from sprint.authenticator.logic import singup
from sprint.authenticator.logic import buscarPorOTP
from django.http import JsonResponse
from .forms import LoginForm
from .forms import SingupForm

# Create your views here.
def crearDatosInciales(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            otp = ""
            num1 = str(random.randint(0, 9))
            otp += num1
            num2 = str(random.randint(0, 9))
            otp += num2
            num3 = str(random.randint(0, 9))
            otp += num3
            num4 = str(random.randint(0, 9))
            otp += num4
            num5 = str(random.randint(0, 9))
            otp += num5
            name = form["nombres"].value()
            apellidos = form["apellidos"].value()
            pais = form["pais"].value()
            ciudad = form["ciudad"].value()
            correo = form["correo"].value()
            numero = form["numero"].value
            data = {
                "datos recibidos"
            }
            login(name, apellidos, pais, ciudad, correo, numero, otp)
            messages.add_message(request, messages.SUCCESS, "Creado exitosamente")
            return JsonResponse(data)
        else:
            print(form.errors)

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
            singup(existe, profesion, actividad, empresa, ingresos, deudas, idData)
            messages.add_message(request, messages.SUCCESS, "Creado exitosamente")
            respuesta = {"respuesta": "creado exitosamente"}
            return JsonResponse(respuesta)
        else:
            print(form.errors)