from django.db import models

# Create your models here.
class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.value, self.value)

class AutenticacionSolicitud(models.Model):
    solicitud = models.OneToOneField(Solicitud, on_delete=models.CASCADE, primary_key=True)
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    estado_autenticacion = models.BooleanField(default=False)
    notas_autenticacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.value, self.value)

class ProcesamientoSolicitud(models.Model):
    autenticacion = models.OneToOneField(AutenticacionSolicitud, on_delete=models.CASCADE, primary_key=True)
    aprobacion = models.BooleanField(default=False)
    notas_procesamiento = models.TextField(blank=True, null=True)
    respuesta_texto = models.TextField()
    
    def __str__(self):
        return '%s %s' % (self.value, self.value)

class RegistroSolicitud(models.Model):
    procesamiento_solicitud = models.ManyToManyField(ProcesamientoSolicitud)

    def __str__(self):
        return '%s %s' % (self.value, self.value)