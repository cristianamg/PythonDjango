from django.conf.urls import url

from Partida.views import index, juego


urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^$',juego, name='juego'),
]