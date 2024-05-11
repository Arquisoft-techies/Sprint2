from django.db import models

class Solicitud(models.Model):
    Id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ingresos = models.IntegerField()
    status =  models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)