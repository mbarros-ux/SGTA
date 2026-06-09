# SGTA - Sistema de Gerenciamento de Tarefas Acadêmicas

API REST desenvolvida em Django para gerenciar tarefas acadêmicas e os usuários responsáveis por elas. O sistema permite cadastrar tarefas com status, prioridade e prazo de entrega, além de filtrar e buscar tarefas de diversas formas.

Como Fazer:
ETAPA 1 — Configuração Inicial do Projeto (Sem Docker) 

1. Entrar na pasta do backend 

cd backend 
 

2. Criar ambiente virtual 

python -m venv venv 
 

3. Ativar ambiente virtual (Windows) 

venv\Scripts\activate 
 

4. Instalar dependências 

pip install django djangorestframework psycopg[binary] python-decouple 
 

5. Salvar dependências 

pip freeze > requirements.txt 
 

6. Criar projeto Django 

django-admin startproject config . 
 

7. Criar app principal 

Substitua seuapp pelo nome do seu projeto (ex.: tarefas, produtos, clientes, etc.) 

python manage.py startapp seuapp 
 

 

ETAPA 2 — Modelagem e Banco de Dados 

Arquivos a modificar 

seuapp/models.py 

seuapp/admin.py 

seuapp/views.py 

config/urls.py 

Arquivo a criar 

seuapp/urls.py 

Configurações 

1. Criar a entidade no model 

Editar: 

seuapp/models.py 
 

Criar sua entidade com pelo menos: 

um campo choices 

os demais campos necessários para o projeto 

2. Registrar o app 

Editar: 

config/settings.py 
 

Adicionar em: 

INSTALLED_APPS = [ 
   ... 
   'seuapp', 
] 
 

3. Executar migrações 

Gerar migrações: 

python manage.py makemigrations 
 

Aplicar ao banco: 

python manage.py migrate 
 

4. Criar superusuário 

python manage.py createsuperuser 
 

5. Rodar o servidor 

python manage.py runserver 
 

6. Cadastrar registros 

Acessar: 

http://127.0.0.1:8000/admin 
 

Cadastrar pelo menos 3 registros. 

 

ETAPA 3 — Criação da API (Views + URLs) 

1. Criar views com JsonResponse 

Editar: 

seuapp/views.py 
 

Criar endpoints que retornem JSON. 

2. Criar rotas 

Criar: 

seuapp/urls.py 
 

Exemplo: 

from django.urls import path 
from . import views 
 
urlpatterns = [ 
   path('seus-itens/', views.listar_itens), 
] 
 

3. Incluir rotas no projeto 

Editar: 

config/urls.py 
from django.contrib import admin 
from django.urls import path, include 
 
urlpatterns = [ 
   path('admin/', admin.site.urls), 
   path('api/', include('seuapp.urls')), 
] 
 

4. Reiniciar servidor 

python manage.py runserver 
 

5. Testar no navegador 

http://127.0.0.1:8000/api/seus-itens/ 
 

Resultado esperado: 

{ 
 "mensagem": "API funcionando" 
} 
 

 

ETAPA 4 — Testes com Thunder Client (ou similar) 

4.1 Criar registro (POST) 

Método 

POST 
 

URL 

http://127.0.0.1:8000/tarefas/criar/ 
 

Body 

{ 
 "campo1": "valor", 
 "campo2": "valor" 
} 
 

 

4.2 Atualizar registro (PUT) 

Método 

PUT 
 

URL 

http://127.0.0.1:8000/tarefas/8/atualizar/ 
 

Body 

{ 
 "campo1": "novo valor", 
 "campo2": "novo valor" 
} 
 

 

4.3 Remover registro (DELETE) 

Método 

DELETE 
 

URL 

http://127.0.0.1:8000/tarefas/8/remover/ 
 

 

ETAPA 5 — Migração para Docker + PostgreSQL 

Remover arquivos locais 

Excluir: 

backend/db.sqlite3 
backend/venv/ 
 

 

Estrutura necessária 

Raiz do projeto 

/ 
├── docker-compose.yml 
├── .env 
├── .env.example 
└── backend/ 
 

Dentro de backend 

backend/ 
├── Dockerfile 
├── entrypoint.sh 
├── manage.py 
├── requirements.txt 
└── config/ 
 

 

Variáveis de ambiente 

.env 

DB_NAME=nome_banco 
DB_USER=usuario 
DB_PASSWORD=senha 
 

.env.example 

DB_NAME= 
DB_USER= 
DB_PASSWORD= 
 

Modifique config/settings.py para ler o .env e usar o PostgreSQL 

from decouple import config, Csv 

import os 

  

SECRET_KEY = config('SECRET_KEY') 

DEBUG = config('DEBUG', default=False, cast=bool) 

  

DATABASES = { 

    'default': { 

        'ENGINE': 'django.db.backends.postgresql', 

        'NAME': config('DB_NAME'), 

        'USER': config('DB_USER'), 

        'PASSWORD': config('DB_PASSWORD'), 

        'HOST': config('DB_HOST'), 

        'PORT': config('DB_PORT', default='5432'), 

    } 

} 

 

docker-compose.yml 

services: 
 db: 
   image: postgres:16 
   environment: 
     POSTGRES_DB: ${DB_NAME} 
     POSTGRES_USER: ${DB_USER} 
     POSTGRES_PASSWORD: ${DB_PASSWORD} 
   volumes: 
     - postgres_data:/var/lib/postgresql/data 
   healthcheck: 
     test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"] 
     interval: 5s 
     timeout: 5s 
     retries: 5 
 
 web: 
   build: ./backend 
   volumes: 
     - ./backend:/app 
   ports: 
     - "8000:8000" 
   env_file: 
     - .env 
   depends_on: 
     db: 
       condition: service_healthy 
   command: > 
     sh -c "python manage.py migrate && 
            python manage.py runserver 0.0.0.0:8000" 
 
volumes: 
 postgres_data: 
 

 

Configurar PostgreSQL no Django 

Editar: 

backend/config/settings.py 
from decouple import config 
 
DATABASES = { 
   'default': { 
       'ENGINE': 'django.db.backends.postgresql', 
       'NAME': config('DB_NAME'), 
       'USER': config('DB_USER'), 
       'PASSWORD': config('DB_PASSWORD'), 
       'HOST': 'db', 
       'PORT': '5432', 
   } 
} 
 

 

Comandos Docker 

(Opcional) Exportar dados do SQLite 

python manage.py dumpdata seuapp --indent 4 > dados.json 
 

Subir containers 

docker compose down 
docker compose up --build 
 

Importar dados no PostgreSQL 

docker compose exec web python manage.py loaddata dados.json 
 

Criar superusuário 

docker compose exec web python manage.py createsuperuser 
 

 

ETAPA 6 — Versionamento no GitHub 

Inicializar repositório 

git init 
 

Adicionar arquivos 

git add . 
 

Criar commit 

git commit -m "Migração para Docker e PostgreSQL concluída" 
 

Definir branch principal 

git branch -M main 
 

Conectar ao GitHub 

git remote add origin https://github.com/mbarros-ux/SEU-REPOSITORIO.git 
 

Enviar projeto 

git push -u origin main 
 

 

ETAPA 7 — Publicar Imagem no Docker Hub 

Criar tag da imagem 

Substitua mbarrosdev pelo seu usuário do Docker Hub. 

docker tag sgta-web:latest mbarrosdev/sgta-web:v1 
 

Login 

docker login 
 

Enviar imagem 

docker push mbarrosdev/sgta-web:v1 
 

 

Outra pessoa executando sua imagem 

Baixar imagem 

docker pull mbarrosdev/sgta-web:v1 
 

Executar container 

docker run -p 8000:8000 mbarrosdev/sgta-web:v1 
 

 

Distribuição via arquivo .tar 

Exportar imagem 

docker save -o sgta-web.tar sgta-web:latest 
 

Importar em outra máquina 

docker load -i sgta-web.tar 
 