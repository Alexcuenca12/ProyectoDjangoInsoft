from django.urls import path,include
from . import views

urlpatterns = [

    path('urlRegistro/',views.create, name='urlRegistroCatalogo'),
    path('urlCosultar/',views.consultar , name='urlCosultarCatalogo'),

]