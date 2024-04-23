import datetime

from .models import *

from django.http import HttpResponse, JsonResponse

def get_datetime(request):
    return HttpResponse(datetime.datetime.utcnow())

def get_texto(request, texto):
    return HttpResponse("O texto escolhido foi '{}'".format(texto))

def get_usuarios(request):
    usuarios = Usuario.objects.all().values('nomeCompleto', 'cpf', 'email')

    resposta = "== BANCO DE DADOS ==\n"
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

def delete_usuario(request, cpf):
    usuario = Usuario.objects.get(cpf=cpf)

    nomeCompleto = usuario.nomeCompleto

    usuario.delete()

    return HttpResponse("Usuario {} deletado com sucesso".format(nomeCompleto))

def update_usuario(request, cpf):
    novo_email = request.GET['email']

    Usuario.objects.filter(cpf=cpf).update(email=novo_email)

    return HttpResponse("Dados do usuario atualizado")
