from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import EnCatalogo, EnTipoCatalogo


# Create your views here.
def create(request):

    listaTipoCatalogo = list(EnTipoCatalogo.objects.values())

    data = {
        'titulo': 'Registro de Catalogos',
        'listaTipoCatalogo': listaTipoCatalogo,
    }

    return HttpResponse(request,'registroCatalogo.html' ,data)


def consultar(request):

    catalogos = list(EnCatalogo.objects.values())
    data = {
        'titulo': 'Lista de Catalogos',
        'catalogos': catalogos,
    }

    # return JsonResponse(catalogos, safe=False)
    return render(request,'consultarCatalogo.html',data)
def buscar(request ,nombre):
    # catalogo = get_object_or_404(EnCatalogo,nombre=nombre)
    catalogo = EnCatalogo.objects.get(nombre=nombre)
    return JsonResponse('catalogo :  %s' % catalogo.nombre)




