<p align="center">
  <img src="https://github.com/petsi-each/Microcontroladores-ESP32/raw/master/logo.png" width="150" /><br/>
  <b>Workshop de Introdução ao Django</b><br/>
  <i>Owlficinas (PET-SI) e Semana de Sistemas de Informação (SSI)</i>
</p>

# :dart: Objetivo

Este workshop foi organizado pela Semana de Sistemas de Informação (SSI) com apoio do PET-SI para os membros de Infraestrutura da SSI e estudantes da EACH-USP com o pré-requisito de conhecimentos em lógica de programação.

Ao finalizar o curso, você:
- Criará sua primeira API utilizando Django
- Implementará seu primeiro banco de dados
- Entenderá sobre a arquitetura de servidores e clientes

<br/><br/>

# :bookmark_tabs: Sumário de tópicos
1. Instalar ferramentas
	1. Python3
	2. Django
2. Servidores Web 
3. Projeto e Aplicação
	1. :bulb: *Desafio*: criar um projeto Django
	2. :bulb: *Desafio*: criar uma aplicação Django
4. Criando primeiro fluxo :bulb: *Desafio*
	1. Criar uma view
	2. Criar uma url
6. Banco de dados
	1. :bulb: *Desafio*: Criação das tabelas
7. Fluxo com parâmetros
	1. :bulb: *Desafio*: criar fluxo com parâmetros
8. CRUD
	1. :bulb: *Desafio*: Read
	2. :bulb: *Desafio*: Create 
	3. :bulb: *Desafio*: Delete
	4. :bulb: *Desafio*: Update
9. Comandos mais utilizados
	1. Rodar projeto Django
	2. Trocar de branch
	3. Verificar alterações

<br/><br/>

# :computer: Conteúdo

## :electric_plug: 1. Instalar ferramentas

### **Python**

Verificar se já veio instalado

```shell
python --version
```

### **Django**

Instalar:

```shell
python -m pip install Django
```

Verificar se foi instalado:

```shell
python -m django --version
```

<br/>

## :cloud: 2. Servidores Web

![image](https://github.com/petsi-each/workshop-django/assets/62656745/53b54d5f-0427-4cd3-b176-1589991b6997)

Comunicação: por meio de troca de mensagens

<br/>

## :bell: 3. Projeto e Aplicação

**Projeto Django**: um conjunto de aplicações.
**Aplicações**: serviços que vão estar rodando no servidor.

### Criando projeto Django 

> 🌱 Branch: etapa0

```shell
django-admin startproject saphira
```

Diretórios e arquivos criados:

![Estrutura de repositórios criada](https://github.com/Anemaygi/workshop-django/assets/62656745/1794f390-3aac-48f0-99f0-eb262b6d23b4)

Rodar projeto:
Abrir diretório do arquivo `manage.py`

```shell
cd /workspaces/workshop-django/saphira/
```
``
```shell
python manage.py runserver
```

### Criando uma Aplicação

> 🌱 Branch: etapa1

```shell
python manage.py startapp api
```

Estrutura de diretórios criada:

![Estrutura de repositórios criada](https://github.com/Anemaygi/workshop-django/assets/62656745/93ec070b-9e17-4b29-a791-939e8a7eac92)

Principais arquivos: **urls** e **views**

Configurações em `saphira/settings.py`

<br/>

## :loop: 4. Criando primeiro fluxo 

> 🌱 Branch: etapa2

### Criar uma view

Arquivo: `api/views.py`

```python
import datetime

from django.http import HttpResponse, JsonResponse

def get_datetime(request):
    return JsonResponse({"datetime": datetime.datetime.utcnow()})
```

### Criar url

Arquivo: `api/urls.py`

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_datetime, name="get_datetime"),
]
```

#### Configurações em `saphira/urls.py`

```python
from django.urls import include
```

```python
path("api/", include("api.urls"))
```

## :game_die: 5. Banco de dados 

> 🌱 Branch: etapa3

As configurações do banco de dados estão em `saphira/settings.py`

Adicionar aplicação *api* no projeto *Saphira* `settings.py`:

```python
api.apps.ApiConfig
```

### Tabelas

Adicionar tabelas do banco de dados: `api/models.py`

```python
from django.db import models

class Usuario(models.Model):
    nomeCompleto = models.CharField(max_length=200)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)

class Palestra(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()

class Presenca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    palestra = models.ForeignKey(Palestra, on_delete=models.CASCADE)
    presencial = models.BooleanField(default=False)
```

![2](https://github.com/petsi-each/workshop-django/assets/62656745/b28260d9-39c2-4646-8be2-c2df294cf229)

**Make migration**: informar ao Django que foram realizadas alterações no banco de dados.

```ssh
python manage.py makemigrations api
```

Ver alterações feita pela migração:

```ssh
python3 manage.py sqlmigrate api 0001
```

Fazer migração:

```ssh
python manage.py migrate
```

<br/>

## :loop: 6. Fluxo com parâmetros 

> 🌱 Branch: etapa4

Adicionar uma nova *url* `api/urls.py`

```python
path("texto/<texto>", views.get_texto, name="get_texto")
```

Adicionar uma nova *view* `views.py`

```python
def get_texto(request, texto):
	return HttpResponse("O texto escolhido foi '{}'".format(texto))
```

<br/>

## :computer_mouse: 7. CRUD

### Read 

> 🌱 Branch: etapa5

Objetivo: pegar todos os usuários cadastrados no banco de dados

Adicionar uma nova *url* `api/urls.py`

```python
path("usuarios", views.get_usuarios, name="get_usuarios")
```

Adicionar uma nova *view* `api/views.py`

```python
from .models import *


def get_usuarios(request):
    usuarios = Usuario.objects.all().values('nomeCompleto', 'cpf', 'email')

    resposta = "= BANCO DE DADOS =\n"
    for usuario in usuarios:
        resposta += f"Nome: {usuario['nomeCompleto']}, CPF: {usuario['cpf']}, E-mail: {usuario['email']}\n"

    return HttpResponse(resposta, content_type="text/plain")
```


### Create

> 🌱 Branch: etapa6

Request Parameters
```
/api?email=franciscoogjr@usp.br&nomeCompleto=Francisco%20Gomes
```

Adicionar uma nova *url* `api/urls.py`

```python
path("usuario/add", views.add_usuario, name="add_usuario")
```

Adicionar uma nova *view* `api/views.py`

```python
def add_usuario(request):
    nomeCompleto = request.GET['nomeCompleto']
    email = request.GET['email']
    cpf = request.GET['cpf']

    novo_usuario = Usuario(nomeCompleto=nomeCompleto, email=email, cpf=cpf)

    novo_usuario.save()  

    return JsonResponse({'mensagem':f'{nomeCompleto} cadastrado'})
```

Nova rota:
```
api/usuario/add?nomeCompleto=&email=&cpf=
```

### Delete 

> 🌱 Branch: etapa7

```python
path("usuario/delete/<cpf>", views.delete_usuario, name="delete_usuario")
```

Adicionar uma nova *view* `api/views.py`

```python
def delete_usuario(request, cpf):
    usuario = Usuario.objects.get(cpf=cpf)

    nomeCompleto = usuario.nomeCompleto

    usuario.delete()

    return HttpResponse("Usuario {} deletado com sucesso".format(nomeCompleto))
```

### Update 

> 🌱 Branch: etapa8

```python
path("usuario/update/<cpf>", views.update_usuario, name="update_usuario")
```

```python
def update_usuario(request, cpf):
    novo_email = request.GET['email']

    Usuario.objects.filter(cpf=cpf).update(email=novo_email)

    return HttpResponse("Dados do usuario atualizado")
```

<br/>

## :keyboard: Comandos mais utilizados

### Rodar projeto Django

Entrada no diretório do arquivo `manage.py`:

```shell
cd /workspaces/workshop-django/saphira/
```

Comando runserver
``
```shell
python manage.py runserver
```

### Trocar de branch

```bash
git checkout <nome_da_branch>
```

### Verificar alterações

```bash
git diff
```


<br/>

# :books: Referências e materiais complementares

- [Documentação oficial do Django](https://docs.djangoproject.com/en/5.0/)
- [Query-parameters](https://djangocentral.com/capturing-query-parameters-of-requestget-in-django/)

