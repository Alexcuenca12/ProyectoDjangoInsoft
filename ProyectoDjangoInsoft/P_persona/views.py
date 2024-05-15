from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    data= {
        'name' : 'abel gomez ',
        'datos': 'mas datos  ',
    }

    # configurar en settings  para que reconosca nuenstra plantillas
    #es opcionales mandar parametro
    return render(request, 'index.html', data)

def registarPersona(request):
    data = {
        'name': 'abel gomez ',
        'datos2': 'mas datos 2 . ',
    }
    return render(request, 'second.html', data)


