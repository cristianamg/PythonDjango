# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class player(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class tablero(models.Model):
    tamano = models.CharField(max_length=50)