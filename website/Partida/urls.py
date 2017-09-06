from django.conf.urls import url

from Partida.views import index

urlpatterns = [
    url(r'^$',index),

]