# Workshop Django

# Tópicos
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
	5. *Desafio*: criar um projeto Django
	7. urls.py
4. Criando aplicação Django
	1. *Desafio*: criar uma aplicação Django
	2. Preparar ambiente
		1. criar api/urls.py
		2. Configurações em saphira/settings.py
			1. *Desafio*: adicionar aplicação em INSTALLED_APPS
	3. views.py
		2. *Desafio*: criar uma view get_datetime
		2. JsonResponse
	4. urls.py
		1. Função django.urls.path: rota e view
		2. *Desafio*: Criar um endpoint get_datetime

5. settings.py
	
6. models.py
	8. *Desafio*: implementar tabelas do banco de dados
7. Migrate
	1. *Desafio*: realizar migração
8. Aprimorando aplicação
	1. urls com parâmetros
	2. views com parâmetros
	3. *Desafio*: implementar fluxo com parâmetros
9. Implementar CRUD

# Roteiro
## Instalar ferramentas
**Python**
Verificar se já veio instalado
```
python --version
```
**Django**
Instalar:
```
python -m pip install Django
```
Verificar se foi instalado:
```
python -m django --version
```
**curl**
Verificar se já veio instalado
```
curl --version
```

## Servidores Web
Canva: link
Componentes:
- Cliente / Front
- Aplicação
- Banco de dados

## Projeto e Aplicação
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

## Criando primeiro flixo
### Criar uma view
Arquivo: *api/views.py*
```
import datetime

from django.http import HttpResponse

def get_datetime(request):
    return JsonResponse({"datetime": datetime.datetime.utcnow()})
```
### Criar api/urls.py

1. Preparar ambiente
	1. criar api/urls.py
	2. Configurações em saphira/settings.py
		1. *Desafio*: adicionar aplicação em INSTALLED_APPS
# Tarefas
*Material*
- [] - Planejar e documentar explicação sobre Servidores Web
- [] - Descrever principais arquivos (urls e views) ao criar uma aplicação
**Documentação**
- [] - No README, alterar demonstração da árvore de diretórios, usar print do vscode