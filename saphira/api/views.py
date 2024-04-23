import datetime

from .models import *

from django.http import HttpResponse, JsonResponse

def get_datetime(request):
    return JsonResponse({"datetime": datetime.datetime.utcnow()})

def get_texto(request, texto):
    return HttpResponse("O texto escolhido foi '{}'".format(texto))

def get_usuarios(request):
    usuarios = Usuario.objects.all().values('nomeCompleto', 'cpf', 'email')

    resposta = "="
    for usuario in usuarios:
        resposta += f"Nome: {usuario['nomeCompleto']}, CPF: {usuario['cpf']}, E-mail: {usuario['email']}\n"

    return HttpResponse(resposta, content_type="text/plain")
