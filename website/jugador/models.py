# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class jugador(models.Model):
    IDJugador = models.IntegerField()
    NickName = models.CharField(max_length=50)
    CantidadGanes = models.IntegerField()
    CantidadJuegos = models.IntegerField()