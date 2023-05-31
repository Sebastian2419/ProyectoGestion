from django.db import models

# Create your models here.

class Liga(models.Model):
    temporada = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    equipo_local = models.CharField(max_length=50)
    equipo_visitante = models.CharField(max_length=50)
    goles_local = models.CharField(max_length=50)
    goles_visitante = models.CharField(max_length=50)
    ganador = models.CharField(max_length=50)
