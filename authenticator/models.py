from typing import Any
from django.db import models

# Create your models here.
class Login(models.Model): #Autenticacion
    nombres = models.CharField(max_length = 50) 
    apellidos = models.CharField(max_length = 50) 
    pais =  models.CharField(max_length = 50) 
    ciudad = models.CharField(max_length = 50) 
    correo = models.CharField(max_length = 50) 
    numero = models.CharField(max_length = 10)
    def __str__(self):
        return '%s %s' % (self.value, self.value)

class Signup(models.Model): #Info Básica
    profesion = models.CharField(max_length = 50)
    actividadEconomica = models.CharField(max_length = 50) 
    empresa = models.CharField(max_length = 50) 
    ingresos = models.FloatField()
    deudas = models.FloatField()
    
    def __str__(self):
        return '%s %s' % (self.value, self.value)
    
    
class DatosInicial(models.Model): #Se creo para poder hacer el ejercicio de persistencia.
    nombres = models.CharField(max_length = 50) 
    apellidos = models.CharField(max_length = 50) 
    pais =  models.CharField(max_length = 50) 
    ciudad = models.CharField(max_length = 50) 
    correo = models.CharField(max_length = 50) 
    numero = models.CharField(max_length = 10)
    profesion = models.CharField(max_length = 50)
    actividadEconomica = models.CharField(max_length = 50) 
    empresa = models.CharField(max_length = 50) 
    ingresos = models.IntegerField()
    deudas = models.IntegerField()
    otp = models.CharField(max_length = 50)
    
    def __init__(nombres, apellidos, pais, ciudad, correo, numero, profesion, actividad, empresa, ingresos, deudas, otp) -> None:
        super().__init__(nombres, apellidos, pais, ciudad, correo, numero, profesion, actividad, empresa, ingresos, deudas, otp)
    
