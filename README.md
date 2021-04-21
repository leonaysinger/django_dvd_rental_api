# Django DVD Rental API *** em desenvolvimento ***

API em Django para acesso ao dvd rental

## Objetivo

O principal objetivo é o estudo do framework Django, criando um sistema backend de API que conecta a um banco de dados Postgres, rodando em um Docker.
O banco utilizado é o dvd rental, que pode ser encontrado aqui: https://www.postgresqltutorial.com/postgresql-sample-database/ .
Com a construção desta API, um front-end será construido para acessá-la. O objetivo é utilizar projetos diferentes implementados em
React, VueJs e Angular.

## Características

Três serviços (container docker) são instanciados via docker compose:
* **db**: Banco de dados postgres versão 11. Na pasta scripts, há todo o backup do banco de dados. Para realizar o backup,
basta copiar o conteúdo da pasta rental_api/scripts para a pasta docker-entrypoint-initdb.d. A imagem do docker do postgres automaticamente
roda os arquivos .sql dentro desta pasta. Necessário também dar permissão de leitura a ela. Estes comandos são realizados 
no arquivo Dockerfile, que remete a instalação da imagem do banco.
* **pgadmin**: API  gráfica para acesso ao banco de dados. Ele depende da instalção correta do banco. Pode ser acessado em **localhost:5050**
* **web**: Imagem que contém o código da aplicação. O arquivo de configuração Dockerfile-application é responsável por 
criar a imagem. No arquivo docker-compose.yml, o command sobrepõe o comando default da imagem docker. Neste caso ele entra 
em sleep por 12 segundos, para certificar que o banco que está com o backup realizado e roda as configurações iniciais do django.
A API pode ser acessada via **localhost:8000** 

## Instalação

Para rodar os serviços, vá para a pasta rental_api, onde estão os arquivos Docker, e rode o comando

``docker-compose up``

