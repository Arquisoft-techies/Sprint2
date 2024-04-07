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