from django.db import models

# Create your models here.
class Login(models.Model):
    nombres = models.CharField(max_length = 50) 
    apellidos = models.CharField(max_length = 50) 
    pais =  models.CharField(max_length = 50) 
    ciudad = models.CharField(max_length = 50) 
    correo = models.CharField(max_length = 50) 
    numero = models.CharField(max_length = 10)
    def __str__(self):
        return '%s %s' % (self.value, self.value)

class Signup(models.Model):
    profesion = models.CharField(max_length = 50)
    actividadEconomica = models.CharField(max_length = 50) 
    empresa = models.CharField(max_length = 50) 
    ingresos = models.FloatField()
    deudas = models.FloatField()
    
    def __str__(self):
        return '%s %s' % (self.value, self.value)


#Para Considerar: 
#El autenticador recibiría los parámetros pasados al login y vería si el usuario se encuentra registrado
#Si se encuentra registrado, va a la página de signup y le muestra su información
#De lo contrario, le muestra los campos vacíos para que los llene.