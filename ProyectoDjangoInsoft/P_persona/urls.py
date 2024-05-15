
from django.urls import path

from P_persona.views import index, registarPersona

urlpatterns = [

    path('urlhomepersona/', index),
    path('urlresgitro/', registarPersona)




]