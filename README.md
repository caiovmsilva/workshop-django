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
	3. curl (ferramenta pra fazer requisições RESTs)
2. Servidores Web 
	1. Componentes: Aplicação, Banco de Dados
	2. Comunicação entre Cliente <-> Aplicação
		1. Tipos de requisições
		2. JSON para enviar e receber dados
	3. Comunicação entre Aplicação <-> Banco de Dados
3. Criando projeto Django
	1. :bulb: *Desafio*: criar um projeto Django
	2. urls.py
4. Criando aplicação Django
	1. *Desafio*: criar uma aplicação Django
	2. Preparar ambiente
		1. criar api/urls.py
		2. Configurações em saphira/settings.py
			1. :bulb: *Desafio*: adicionar aplicação em INSTALLED_APPS
	3. api/views.py
		1. :bulb: *Desafio*: criar uma view get_datetime
		2. JsonResponse
	4. api/urls.py
		1. Função django.urls.path: rota e view
		2. *Desafio*: Criar um endpoint get_datetime
	5. saphira.urls.py
		1. Adicionar urls da aplicação api
6. models.py
	1. *Desafio*: implementar tabelas do banco de dados
7. Migrate
	1. *Desafio*: realizar migração
8. Aprimorando aplicação
	1. urls com parâmetros
	2. views com parâmetros
	3. *Desafio*: implementar fluxo com parâmetros
9. Implementar CRUD

<br/><br/>

# :computer: Conteúdo

## :electric_plug: 1. Instalar ferramentas

### **Python**

Verificar se já veio instalado

```
python --version
```

### **curl**

Verificar se já veio instalado

```
curl --version
```

### **Django**

Instalar:
```
python -m pip install Django
```
Verificar se foi instalado:
```
python -m django --version
```


## :cloud: 2. Servidores Web

Canva: link

Componentes:
- Cliente / Front
- Aplicação
- Banco de dados

## :bell: 3. Projeto e Aplicação

**Aplicações**: serviços que vão estar rodando no servidor.

**Projeto Django**: um conjunto de aplicações.

### Criando projeto Django
```
django-admin startproject saphira
```
Diretórios e arquivos criados:
```
saphira/
    saphira/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
        manage.py
```

Rodar projeto:

```
python manage.py runserver
```

### Criando uma Aplicação

```
python manage.py startapp api
```

Estrutura de diretórios criada:

```
api/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Principais arquivos:

- **urls**:
- **views**:

## :loop: 4. Criando primeiro fluxo

### Criar uma views da Aplicação

Arquivo: *api/views.py*
```
kimport datetime

from django.http import HttpResponse, JsonResponse

def get_datetime(request):
    return JsonResponse({"datetime": datetime.datetime.utcnow()})
```

### Criar urls da Aplicação

Arquivo: api/urls.py

```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_datetime, name="get_datetime"),
]
```

### Configurações em saphira/urls.py

```
path("api/", include("api.urls")),
```

## :game_die: 5. Banco de dados

As configurações do banco de dados estão em saphira/settings.py.

### Tabelas

Usuario
- nomeCompleto
- email
- cpf

Palestra
- titulo
- descriçao

Presença
- Usuario
- Palestra
- presencial

<br/><br/>

# :books: Referências e materiais complementares

- [Documentação oficial do Django](https://docs.djangoproject.com/en/5.0/)
