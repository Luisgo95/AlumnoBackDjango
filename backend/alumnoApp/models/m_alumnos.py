from django.db import models



class Alumno(models.Model):
    carnet = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    genero = models.CharField(max_length=250)
    telefono = models.CharField(max_length=250)
    fechaNacimiento = models.DateTimeField(auto_now=False)
    generoPoesia = models.CharField(max_length=250)
    carrera = models.CharField(max_length=250)
    fechaInscripcion = models.DateTimeField(auto_now=False)
    fechaExposicion = models.DateTimeField(auto_now=False)
  

    def __unicode__(self):
        return self.nombre

    # def delete(self, *args):
    #     self.activo = False
    #     self.save()
    #     return True