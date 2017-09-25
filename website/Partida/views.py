# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect



# Create your views here.
from Partida.models import Partida
from jugador.models import jugador


def index(request):
    partidas = Partida.objects.all()
    jugadores = jugador.objects.all()
    contexto = {'partidas':partidas,'jugadores':jugadores}


    return render(request, 'PantallaPrincipal/principal.html',contexto)

def juego(request):
    partidas = Partida.objects.all()
    jugadores = jugador.objects.all()
    contexto = {'partidas':partidas,'jugadores':jugadores}

    return render(request, 'Juego/juego.html',contexto)
