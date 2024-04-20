import datetime

from .models import *

from django.http import HttpResponse, JsonResponse

def get_datetime(request):
    return JsonResponse({"datetime": datetime.datetime.utcnow()})

def get_texto(request, texto):
    return HttpResponse("O texto escolhido foi '{}'".format(texto))

def get_usuarios(request):

    usuarios = [usurio.nomeCompleto for usurio in Usuario.objects.all()]

    return JsonResponse(usuarios, safe=False)

def add_usuario(request):

    nomeCompleto = request.GET['nomeCompleto']
    email = request.GET['email']
    cpf = request.GET['cpf']

    novo_usuario = Usuario(nomeCompleto=nomeCompleto, email=email, cpf=cpf)

    novo_usuario.save()

    return JsonResponse({'mensagem':f'{nomeCompleto} cadastrado'})