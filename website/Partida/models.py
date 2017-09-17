# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Partida(models.Model):
    IDJugadorUno = models.IntegerField()
    IDJugadorDOs = models.IntegerField()
    CantFichasLinea = models.IntegerField()
    TamannoTablero = models.IntegerField()
    IDGanador = models.CharField(max_length=50)
    EstadoTablaFinal = models.CharField(max_length=1000)
    Turno = models.CharField(max_length=10)
    Estado = models.CharField(max_length=10)
    ListaMovimientos = models.CharField(max_length=1000)
