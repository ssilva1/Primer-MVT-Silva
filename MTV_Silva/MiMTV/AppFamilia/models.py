from django.db import models

class Familia(models.Model):
    
    nombre_y_apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
