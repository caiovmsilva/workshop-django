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

def add_usuario(request):

    nomeCompleto = request.GET['nomeCompleto']
    email = request.GET['email']
    cpf = request.GET['cpf']

    novo_usuario = Usuario(nomeCompleto=nomeCompleto, email=email, cpf=cpf)

    novo_usuario.save()

    return HttpResponse("Cadastro de {} realizado com sucesso".format(nomeCompleto))
