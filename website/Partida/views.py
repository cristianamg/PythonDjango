# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect


from Partida.forms import PartidaForm



# Create your views here.
from Partida.models import Partida
from jugador.models import jugador


def index(request):
    partidas = Partida.objects.all()
    jugadores = jugador.objects.all()
    contexto = {'partidas':partidas,'jugadores':jugadores}


    return render(request, 'PantallaPrincipal/principal.html',contexto)

def partidaView(request):

    if request.method == 'POST':
        form = PartidaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Partida:index')
    else:
        form = PartidaForm()

    return render(request,'PantallaPrincipal:principal.html',{'form':form})