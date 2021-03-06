"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from Partida.views import juego

urlpatterns = [
    url(r'^', include('autenticar.urls')),
    url(r'^accounts/profile/', include('Partida.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^principal/', include('Partida.urls')),
    url(r'^juego/',juego, name="juego"),
    url(r'^game/', include('NLinea.urls')),
    url(r'^logout/$', views.logout, {'next_page': '/'}),

]
