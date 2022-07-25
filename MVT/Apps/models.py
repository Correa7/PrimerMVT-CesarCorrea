from django.db import models

# Create your models here.

class Personas(models.Model):

    vinculo= models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha = models.DateField(auto_now=True, null=True, blank=True)
   