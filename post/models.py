from django.db import models
from datetime import date

class Conductor(models.Model):
  cedula  =  models.IntegerField(max_length=10)
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  telefono =  models.CharField(max_length=200)
  correo =  models.CharField(max_length=200)
  direccion= models.CharField(max_length=200)
  

class Auto (models.Model):
  placa=models.CharField(max_length=6)
  modelo=models.IntegerField(max_length=4)
  marca=models.CharField(max_length=100)
  cedula = models.OneToOneField(Conductor, on_delete= models.CASCADE, primary_key = True, null= False)