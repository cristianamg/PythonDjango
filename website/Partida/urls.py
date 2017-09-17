from django.conf.urls import url

from Partida.views import index, partidaView

urlpatterns = [
    url(r'^$',index, name='index'),
]