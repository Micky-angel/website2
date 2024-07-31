from django.db import models

# Create your models here.


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)  # num de caracteres
    apellido = models.CharField(max_length=50)  # num de caracteres
    carnet = models.IntegerField()  # num
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
