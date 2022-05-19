# django-with-s3-bucket

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=flat&logo=nginx&logoColor=white)](https://www.nginx.com/)

Estudo feito com base [neste artigo](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/).

## O que é

Trata-se de uma simples página de upload de imagem. Ao fazer o upload, a imagem é enviada a um bucket s3.

## O que utiliza

- Docker + docker-compose para orquestração dos containers
- Django para a base do app
- Nginx para servir arquivos estáticos em desenvolvimento caso o `USE_S3` esteja desligado
- Postgres como banco de dados

## Subindo a aplicação e testando

- Crie um arquivo `.env` e o preencha com as variáveis do `.env-sample`
- Basta rodar um `docker-compose up`
- Acesse em seu browser `localhost`
