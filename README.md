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

```bash
python --version
```

### **curl**

Verificar se já veio instalado

```bash
curl --version
```

### **Django**

Instalar:
```bash
python -m pip install Django
```
Verificar se foi instalado:
```bash
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

### Criando projeto Django <span style="color:orange">[etapa0]</span>.
```bash
django-admin startproject saphira
```
Diretórios e arquivos criados:

![Estrutura de repositórios criada](https://github.com/Anemaygi/workshop-django/assets/62656745/1794f390-3aac-48f0-99f0-eb262b6d23b4)


Rodar projeto:

```bash
python manage.py runserver
```

### Criando uma Aplicação <span style="color:orange">[etapa1]</span>

```bash
python manage.py startapp api
```

Estrutura de diretórios criada:

![Estrutura de repositórios criada](https://github.com/Anemaygi/workshop-django/assets/62656745/93ec070b-9e17-4b29-a791-939e8a7eac92)


Principais arquivos:

- **urls**:
- **views**:

## :loop: 4. Criando primeiro fluxo <span style="color:orange">[etapa2]</span>

### Criar uma views da Aplicação

Arquivo: *api/views.py*
```python
import datetime

from django.http import HttpResponse, JsonResponse

def get_datetime(request):
    return JsonResponse({"datetime": datetime.datetime.utcnow()})
```

### Criar urls da Aplicação

Arquivo: api/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_datetime, name="get_datetime"),
]
```

### Configurações em saphira/urls.py

```python
from django.urls import include
```

```python
path("api/", include("api.urls"))
```

## :game_die: 5. Banco de dados <span style="color:orange">[etapa3]</span>

As configurações do banco de dados estão em <span style="color:red">saphira/settings.py</span>

Fazer migração das aplicações já adicionadas:

```python
python manage.py makemigrations api
```

Adicionar aplicação *api* no projeto *Saphira*:

```python
api.apps.ApiConfig
```

### Tabelas

Adicionar tabelas do banco de dados: (<span style="color:red">api/models.py</span>)

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

**Make migration**: informar ao Django que foram realizadas alterações no banco de dados.

```
python manage.py makemigrations api
```

Ver alterações feita pela migração:

```
python3 manage.py sqlmigrate api 0001
```

Fazer migração:

```
python manage.py migrate
```


## :loop: 6. Fluxo com parâmetros

Adicionar uma nova *url* (<span style="color:red">api/urls.py</span>)

```python
path("texto/<texto>", views.get_texto, name="get_texto")
```

Adicionar uma nova *view* (<span style="color:red">api/views.py</span>)

```python
def get_texto(request, texto):
	return HttpResponse("O texto escolhido foi '{}'".format(texto))
```

<br/><br/>

# :books: Referências e materiais complementares

- [Documentação oficial do Django](https://docs.djangoproject.com/en/5.0/)
