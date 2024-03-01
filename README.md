# API de Empresas com Django

Este projeto é uma API desenvolvida com Django Rest Framework que permite realizar operações CRUD (Create, Read, Update, Delete) em um cadastro de empresas. É uma excelente ferramenta para aprender sobre desenvolvimento de APIs com Django.

## Pré-requisitos

Antes de iniciar, você precisará instalar os seguintes pré-requisitos em sua máquina:

- **Python**: A linguagem de programação usada para desenvolver este projeto. [Guia de instalação do Python](https://www.python.org/downloads/).

## Configuração do Ambiente

Siga estas etapas para configurar seu ambiente de desenvolvimento.

### 1. Clone o Repositório

Clone o repositório para sua máquina local usando:

```
git clone https://github.com/JoaoCardoso00/crud-empresas.git
```
navegue até o diretório do projeto:
```
cd crud-empresas
```

### 2. Crie um Ambiente Virtual
Acrie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```
Ative o ambiente virtual:

- No Windows:
```
venv\Scripts\activate
```
- No Linux ou macOS:
```
source venv/bin/activate
```
### 3. Instale as Dependências
Com o ambiente virtual ativado, instale o Django e o Django Rest Framework utilizando o pip:

```
pip install django djangorestframework
```
## Executando o Projeto
Dentro do diretório do projeto e com o ambiente virtual ativado, aplique as migrações do banco de dados:

```
python manage.py migrate
```
Em seguida, inicie o servidor de desenvolvimento:

```
python manage.py runserver
```
Agora você pode acessar a API navegando para http://127.0.0.1:8000/ no seu navegador ou utilizando uma ferramenta como Postman para testar as rotas da API.

## Rotas da API

- `GET /`: Lista todas as empresas.
- `POST /empresa/create`: Cria uma nova empresa.
- `GET /empresa/<int:pk>`: Retorna os detalhes de uma empresa específica.
- `PUT /empresa/<int:pk>/update`: Atualiza os detalhes de uma empresa específica.
- `DELETE /empresa/<int:pk>/delete`: Remove uma empresa do banco de dados.
