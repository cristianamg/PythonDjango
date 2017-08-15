from django.conf.urls import url
from autenticar.views import autenticarIndex

urlpatterns = [
    url(r'^$',autenticarIndex),

]