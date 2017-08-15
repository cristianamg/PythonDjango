from django.conf.urls import url,include
from NLinea.views import index

urlpatterns = [
    url(r'^$',index),

]