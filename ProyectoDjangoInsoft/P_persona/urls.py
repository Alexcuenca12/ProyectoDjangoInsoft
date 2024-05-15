
from django.urls import path

from P_persona.views import index, registarPersona
app_name = 'persona'
urlpatterns = [

    path('urlhomepersona/', index,name='vista1'),
    path('urlresgitro/', registarPersona ,name ='vista2')




]