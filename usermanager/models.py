from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_identificacion = models.IntegerField()
    numero_identificacion = models.IntegerField()
    correo = models.EmailField()
    telefono = models.IntegerField()
    pais = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    actividad_economica = models.CharField(max_length=100)
    ingresos = models.IntegerField()
    deudas = models.IntegerField()
    ciudad = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.value, self.value)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    identificacion = models.IntegerField()
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.value, self.value)
