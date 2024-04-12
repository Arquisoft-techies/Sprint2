from django.db import models

class Signup(models.Model):
    profesion = models.CharField(max_length = 50)
    actividadEconomica = models.CharField(max_length = 50) 
    empresa = models.CharField(max_length = 50) 
    ingresos = models.FloatField()
    deudas = models.FloatField()
    
    def __str__(self):
        return '%s %s' % (self.value, self.value)
