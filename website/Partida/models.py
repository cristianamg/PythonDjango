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
    JugadasP1 = models.CharField(max_length=1000)
    Turno = models.CharField(max_length=10)
    Estado = models.CharField(max_length=10)
    JugadasP2 = models.CharField(max_length=1000)
