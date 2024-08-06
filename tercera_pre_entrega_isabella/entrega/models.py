from django.db import models

# Create your models here.

class Autos(models.Model):
    modelo = models.CharField(max_length=30)
    matricula = models.IntegerField()

class Camiones(models.Model):
    modelo = models.CharField(max_length=30)
    matricula = models.IntegerField()

class Motos(models.Model):
    modelo = models.CharField(max_length=30)
    matricula = models.IntegerField()


